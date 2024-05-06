import pandas as pd
from bokeh.palettes import Category20b
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, FactorRange, Legend, NumeralTickFormatter
from bokeh.io import output_file, save

# List of file paths for the datasets
# file_paths = [
#     "../Data/cykeltaellinger-2005.xlsx",
#     "../Data/cykeltaellinger-2006.xlsx",
#     "../Data/cykeltaellinger-2007.xlsx",
#     "../Data/cykeltaellinger-2008.xlsx",
#     "../Data/cykeltaellinger-2009.xlsx",
#     "../Data/cykeltaellinger-2010.xlsx",
#     "../Data/cykeltaellinger-2011.xlsx",
#     "../Data/cykeltaellinger-2012.xlsx",
#     "../Data/cykeltaellinger-2013.xlsx",
#     "../Data/cykeltaellinger-2014.xlsx",
# ]

file_paths = [
    "Data\cykeltaellinger-2005.xlsx",
    "Data\cykeltaellinger-2006.xlsx",
    "Data\cykeltaellinger-2007.xlsx",
    "Data\cykeltaellinger-2008.xlsx",
    "Data\cykeltaellinger-2009.xlsx",
    "Data\cykeltaellinger-2010.xlsx",
    "Data\cykeltaellinger-2011.xlsx",
    "Data\cykeltaellinger-2012.xlsx",
    "Data\cykeltaellinger-2013.xlsx",
    "Data\cykeltaellinger-2014.xlsx"
]

# List to store DataFrames
dfs = []

# Iterate over file paths, read Excel files, and append to dfs list
for file_path in file_paths:
    data = pd.read_excel(file_path, usecols='A:AD', skiprows=10)
    dfs.append(data)

# Concatenate DataFrames
data_com = pd.concat(dfs, ignore_index=True)
data_com['Total_Value'] = data_com.iloc[:, 6:].sum(axis=1)
data_com['Month'] = pd.to_datetime(data_com['Dato'], format='%d.%m.%Y').dt.month
data_com['year'] =pd.to_datetime(data_com['Dato'], format='%d.%m.%Y').dt.year

data = data_com

month_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun","Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# # Map month numbers to month names
data['Month_Name'] = data['Month'].map({i + 1: month_order[i] for i in range(12)})

data['Month_Name'] = pd.Categorical(data['Month_Name'], categories=month_order, ordered=True)
data = data.sort_values(by='Month_Name')
data['year'] =data['year'].astype(str)
data = data.groupby(['Month_Name', 'year']).agg({'Total_Value': 'sum'}).unstack()
data.columns = data.columns.droplevel()
data.reset_index(inplace=True)  # Resetting the index to flatten the MultiIndex


src = ColumnDataSource(data)

p = figure(x_range=FactorRange(factors=data['Month_Name']), title="Number of bikes counted each month", 
           x_axis_label="Month", y_axis_label="no. Bikes", 
           width=800, height=400)

items = []
bar = {}

for indx, i in enumerate(data.columns[1:]):  # Exclude the 'Month_Name' column
    bar[i] = p.vbar(x='Month_Name', top=i, source=src, color=Category20b[14][indx],
                    muted_alpha=0.005, muted=True, alpha=0.9, width=0.5) 
    items.append((i, [bar[i]]))

legend = Legend(items=items, location='right')
p.add_layout(legend, 'right')

p.legend.click_policy = "mute"
p.y_range.start = 0


# Format y-axis ticks
p.yaxis.formatter = NumeralTickFormatter(format='0')

show(p)

output_file("Bokeh_monthly2.html")
save(p)
