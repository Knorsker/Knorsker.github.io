---
layout: default
---
*Updated: {% assign copenhagen_time = site.time | date: "%d-%m-%Y %H:%M:%S" | date: "%s" | plus: 3600 | date: "%d-%m-%Y %H:%M:%S" %}{{ copenhagen_time }}*


__Introduction (I)__




__Data (II)__\
When analyzing the usage of bikes within Copenhagen, we will be using numerous datasets. The datasets we are using include bike count data, bike stands data, population data, and geoplot data for each city part. All datasets are provided by opendata.dk, except for population data, which is gathered from Københavns Kommunes Statistikbank.

The dataset containing bike counts spans 10 different years, from 2005 to 2014. This data is collected by counters placed on different bike roads within Copenhagen city. The number of bike roads counted varies over the years, as shown in Table 1, which provides an overview of the number of bike roads the data is collected from. This variation is important to take into account when using the data for analysis.


|Year| 2005 | 2006 | 2007 | 2008 | 2009 | 2010 | 2011 | 2012 | 2013 | 2014 | 
|--------|--------|---------|-----------|----------|--------|----------|--------|--------|--------|--------|
|No. Streets|  4  |   12  | 12      | 12     | 13   | 13     | 13   |12   |13   |9   |

_Table 1: Number of streets, where data is measured from._

Secondly we have the population data, this data contains the population number within each city part in Copenhagen over time. We have extracted the quantiles from year 2000 to 2024 to make it possible gain a better understanding of the trends.

Lastly we have the Bike stands data. It contains various information about the number and placement of bike stands in Copenhagen. In addition to this dataset, we have utilized the dataset called 'Bydele' *from opendata.dk*, which includes a GeoJSON file over the different city part of Copenhagen.

__Trends and patterns of XXXXX (III)__
XXX Intro XXX
![One time-series / bar chart](/A3/168hourplot.png)
_Figure 1: A 168 hour barplot showing the patterns for each hour in a week._

Looking at *figure 1* it can clearly be seen that their is a certain pattern for the weekdays each year. The two spikes for each day shows where there is rush hour. Furthermore it also shows that there are fewer that cycle during the weekend. 
It can also be seen that there are more peolple during the night in the weekend compared to night in the weekdays.

![One time-series / bar chart](/A3/monthlyplot.png)
_Figure 2: A monthly barplot showing the number of bikes total whithin that month._

- General fewer bikes in the winter months
- No data in december for year 2005.
- odd low in the first half year of 2006 (Undersøg)
- 2012 has lower density of bikes in the first 5 months

__Comparison (IV)__

XXX Introduction  XXX

<embed 
       type="text/html" 
       src="A3\bokeh_population_spots.html"
       width="1100"
       height="390">
_Figure Y: JFIGURE TEXT._

The first thing that can be seen in the interactive plot is the population of the different districts in Copenhagen. The populations are plotted from year 2000 to year 2024 measured every quarter of the year from 2002 to 2024 and one time in 2000 and 2001. Moreover it is possible to plot accumulated amount of bike spots in the different districts over the years. The start value of the for the accumulated sum is total amount of bike spots with no registration date. 

Looking more detailed at the plot, the main part of the populations are steady over the years, however an increasing can be seen in the districts _Amager Vest_, _Vesterbro - Kongens Enghave_ and _Valby_. From these districts an increasing are respectively calculated to $42983, 30608$ and $19571$. \
Focusing on Amager Vest, it is possible to plot the associated trend in bike spots over the years. It can be seen that there is a small increase in bike racks and bike spots during the years. Specially from July 2014 to February 2017, the amount of bike racks and spots are increasing, though the general increase of bike racks and spots do not follows the increase of population in Amager Vest. \
When plotting the amount of spots and the population for Vesterbro - Kongens Enghave, the amount of bike spots more or less steady from 2001 to 2016. In 2017 a huge change can be seen, which indicates that the municipality made an effort to follow the increase in population. 

__Geographical analysis of bikespot within Copenhagen (V)__


__Discussion and Conclusion (VI)__


__Contributions__

| Part | s214704 | s214725 | s204112 |
|------|---------|---------|---------|
| I    |         |         |         |
| II   |         |         |         |
| III  |         |         |         |
| IV   |         |         |         |

