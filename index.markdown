---
layout: default
---
*Updated: {% assign copenhagen_time = site.time | date: "%d-%m-%Y %H:%M:%S" | date: "%s" | plus: 3600 | date: "%d-%m-%Y %H:%M:%S" %}{{ copenhagen_time }}*


__Introduction (I)__




__Data (II)__\
When analysing the usage of bikes within Copenhagen, we will be using numerous of dataset. The datasets we are using are bike counts data, bikespots data, population data and geoplot data for each city part. All datasets are provided by *opendata.dk* except population, which are gathered from *Københavns Kommunes Statistikbank*.

The dataset containing bike counts are from 10 different years, 2005 to 2014. This data is contained by counters placed on the different bikeroads within Copenhagen city. The number of bikeroads counted from varios over the year, it is possible to see in *table 1* an overview of the number of bikeroads the data is contained from. This variation is important to take into account, when using the data for analysis.


|Year| 2005 | 2006 | 2007 | 2008 | 2009 | 2010 | 2011 | 2012 | 2013 | 2014 | 
|--------|--------|---------|-----------|----------|--------|----------|--------|--------|--------|--------|
|No. Streets|  4  |   12  | 12      | 12     | 13   | 13     | 13   |12   |13   |9   |

_Table 1: Number of streets, where data is measured from._

Secondly we have the population data, this data contains the population number within each city part in Copenhagen.


It contains various information about the number and placement of bike stands in Copenhagen. We have utilized both the CSV file and GeoJSON file to enable various plot options. In addition to these two files, we have also utilized the dataset called 'Bydele,' which includes a GeoJSON file. This file is used to plot the placement and number of bike stands in different parts of the city on a map.

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

