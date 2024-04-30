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


Bikestands/
Lastly we have the Bike stands data. It contains various information about the number and placement of bike stands in Copenhagen. In addition to this dataset, we have utilized the dataset called 'Bydele' *from opendata.dk*, which includes a GeoJSON file over the different city part of Copenhagen.

__Trends and patterns of (III)__
![One time-series / bar chart](/A3/168hourplot.png)
_Figure 1: Barplot._

![One time-series / bar chart](/A3/monthlyplot.png)
_Figure 2: Barplot._


__Comparison (IV)__


__Geographical analysis of bikespot within Copenhagen (V)__


__Discussion and Conclusion (VI)__


__Contributions__

| Part | s214704 | s214725 | s204112 |
|------|---------|---------|---------|
| I    |         |         |         |
| II   |         |         |         |
| III  |         |         |         |
| IV   |         |         |         |

