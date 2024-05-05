import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
import math

#ignore warnings
import warnings
warnings.filterwarnings('ignore')

pd.options.plotting.backend = "plotly"


file = "..\Data\cykelstativ.csv"
df = pd.read_csv(file)

df = df[df["antal_pladser"] != 0]

df.head()

file = "..\Data\Befolkning.csv"
df_befolkning = pd.read_csv(file,sep=',',encoding='latin-1', header=1)

#delete last row of df_befolkning
df_befolkning = df_befolkning[:-1]

#sort by first collumn
df_befolkning = df_befolkning.sort_values(by=' ')

import plotly.express as px
from urllib.request import urlopen
import json

#import cph map
with urlopen('https://wfs-kbhkort.kk.dk/k101/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=k101:bydel&outputFormat=json&SRSNAME=EPSG:4326') as response:
    cph = json.load(response)

#import bikeracks 
with urlopen('https://wfs-kbhkort.kk.dk/k101/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=k101:cykelstativ&outputFormat=json&SRSNAME=EPSG:4326&CQL_Filter=stativ_type%3C%3E%27Bycykelstativ%27') as response:
    bikeracks = json.load(response)

#import bikelanes
with urlopen('https://wfs-kbhkort.kk.dk/k101/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=k101:cykeldata_kk&outputFormat=json&SRSNAME=EPSG:4326') as response:
    bikelanes = json.load(response)

#make df that sums the antal_plader for each district
district_data_O = df[df["stativ_ejer"]=="Offentligt"].groupby("bydel", observed=False)
district_data_P = df[df["stativ_ejer"]=="Privat"].groupby("bydel", observed=False)
district_data = df.groupby("bydel", observed=False)

district_data_O = district_data_O.agg({"antal_pladser": "sum"}).reset_index().sort_values(by='bydel')
district_data_P = district_data_P.agg({"antal_pladser": "sum"}).reset_index().sort_values(by='bydel')
district_data = district_data.agg({"antal_pladser": "sum"}).reset_index().sort_values(by='bydel')

district_data["Offtenlige pladser"] = district_data_O["antal_pladser"]
district_data["Private pladser"] = district_data_P["antal_pladser"]

#add coloum with area of each district
for i in range(len(cph['features'])):

    index = district_data.index[district_data['bydel'] == cph['features'][i]['properties']['navn']].tolist()[0]
    district_data.at[index, 'areal_m2'] = cph['features'][i]['properties']['areal_m2']

district_data['antal_pladser_per_m2'] = district_data['antal_pladser'] / district_data['areal_m2']


district_data["befolkning2024"] = df_befolkning["2024K1"]

district_data["antal_pladser_per_befolkning"] = district_data['antal_pladser'] /df_befolkning["2024K1"]

district_data


# Define your district_data and other necessary variables here
#make list of x and y for eahc feature in bikeracks
lats = []
longs = []
category = []
size = []
cat = "stativ_ejer"


for feature in bikeracks["features"]:
    try:
        lats.append(feature["geometry"]["coordinates"][1])
        longs.append(feature["geometry"]["coordinates"][0])
        category.append(feature["properties"][cat])
        size.append(feature["properties"]["antal_pladser"])
    except:
        continue

assert len(lats) == len(longs)




############# Plot from here, above is data initialization #########

from dash import Dash, dcc, html, Input, Output
import plotly.express as px

app = Dash(__name__)

app.layout = html.Div([
    html.H4('Bike Racks Analysis'),
    html.P("Select a unit:"),
    dcc.RadioItems(
        id='unit',
        options=[
            {'label': 'Number of Bike Racks', 'value': 'antal_pladser'},
            {'label': 'Bike Racks per Square Meter', 'value': 'antal_pladser_per_m2'},
            {'label': 'Bike Racks per Population', 'value': 'antal_pladser_per_befolkning'}
        ],
        value='antal_pladser',
        inline=True
    ),
    dcc.Graph(id="graph"),
])

@app.callback(
    Output("graph", "figure"),
    Input("unit", "value"))
def display_choropleth(unit):
    print("Selected unit:", unit)  # Print the selected unit for debugging

    # Your existing code...
    fig = px.choropleth_mapbox(
        district_data, geojson=cph, color=unit,
        locations="bydel", featureidkey="properties.navn",
        range_color=(0, district_data[unit].max()),
        center={"lat": 55.676098, "lon": 12.568337}, zoom=10.5,
        color_continuous_scale="Viridis", mapbox_style="carto-positron", opacity=0.6)
    
    # Move layout update inside the callback function
    fig.update_layout(
        margin={"r": 0, "t": 0, "l": 0, "b": 0},
        mapbox_accesstoken="pk.eyJ1IjoiczIxNDcyNSIsImEiOiJjbHZ0ZHFiamYwYWNyMmltamtzaG03MGti.cx8eJ2xUoQH1NF4mOjJFKA")

    # Add scattermapbox
    fig.add_scattermapbox(
        lat=lats,
        lon=longs,
        mode='markers+text',
        marker_size=3,
        marker_color='rgb(0, 100, 100)'
    )

    return fig




app.run_server(debug=True)