---
layout: default
---
*Updated: {% assign copenhagen_time = site.time | date: "%d-%m-%Y %H:%M:%S" | date: "%s" | plus: 3600 | date: "%d-%m-%Y %H:%M:%S" %}{{ copenhagen_time }}*


__Introduction (I)__

To get our Notebook click [HERE](A3\Notebook.ipynb)


__Data (II)__\
When analyzing the usage of bikes within Copenhagen, we will be using numerous datasets. The datasets we are using include bike count data, bike stands data, population data, and geoplot data for each city part. All datasets are provided by *opendata.dk*, except for population data, which is gathered from *the City of Copenhagen Statbank*.

The dataset containing bike counts spans 10 different years, from 2005 to 2014. This data is collected by counters placed on different bike roads within Copenhagen city. The number of bike roads counted varies over the years, as shown in Table 1, which provides an overview of the number of bike roads the data is collected from. This variation is important to take into account when using the data for analysis.


|Year| 2005 | 2006 | 2007 | 2008 | 2009 | 2010 | 2011 | 2012 | 2013 | 2014 | 
|--------|--------|---------|-----------|----------|--------|----------|--------|--------|--------|--------|
|No. Streets|  4  |   12  | 12      | 12     | 13   | 13     | 13   |12   |13   |9   |

_Table 1: Number of streets, where data is measured from._

Secondly we have the population data, this data contains the population number within each city part in Copenhagen over time. We have extracted the quantiles from year 2000 to 2024 to make it possible gain a better understanding of the trends.

Lastly we have the Bike stands data. It contains various information about the number and placement of bike stands in Copenhagen. In addition to this dataset, we have utilized the dataset called 'Bydele' from *opendata.dk*, which includes a GeoJSON file over the different city part of Copenhagen.


| | Amager Vest | Amager Øst | Bispebjerg | Brønshøj-Husum | Indre By | Nørrebro | Valby | Vanløse | Vesterbro - Kongens Enghave | Østerbro | 
|--------|-----------|------------|-----------|----------|-----------|----------|--------|--------|--------|--------|
|  Public  |   221  | 125      | 45    | 53   | 864    | 372   |91   |25   |456   | 506 |
|  Private     |   119  | 48     | 150   | 68   | 518    | 418   |111   |75   |438  | 818 |
|  Not registred  |  32  | 76  | 0  | 0   | 296    | 4   |1   |0   |23   | 83 |
| Proportion of public | ~59,4%| ~50,2% | ~23,1% |~43,8%|~51,5%|~46,9%|~44,8%|25%|~49,7%|~36,0%|

_Table 2: Amount of public, private and not registred bike racks._




__Temporal Trends and Seasonal Patterns of bike Activity in Copenhagen (III)__\
XXX Intro XXX
![One time-series / bar chart](/A3/168hourplot.png)
_Figure 1: A 168 hour barplot showing the patterns for each hour in a week._

Examining *Figure 1*, a distinct pattern gradually becomes apparent, revealing consistent trends for weekdays across each year. The appearance of two distinct peaks on each weekday serves as a clear indicator of rush hour periods, indicating peak times of cycling activity within the city. Furthermore, a noticeable decrease in the number of cyclists is observed during the weekends. Additionally, it's visible that more people are out cycling at night on weekends compared to weekdays. This could be because of the city's nightlife and social events.

<embed 
       type="text/html" 
       src="A3\Bokeh_monthly.html"
       width="600"
       height="400">
_Figure 2: Monthly bar plot illustrating total number of bikes for each month.._

To gain better insight into the biking habits of people in Copenhagen throughout the year, a bar plot is created for each year with available data, see *figure 2*. The plot shows the number of bikes counted in Copenhagen for each month, where it is possible to selcet the desired year in the box beside the plot. 

Examining the *figure 2*, it is evident that some of the data is insufficient. For instance, in 2005, there are no recorded bike counts in December. Additionally, an odd number of bike counts from Febuary to May in year 2012, which are notably lower compared to neighboring months and years. Similarly, 2006 exhibits a lower density of bikes in the first five months. For 2010, we see a low number of bikes in the early months.

Several factors may contribute to these variations over the years. For instance in 2012, a [local article](https://www.dr.dk/nyheder/vejret/februar-er-historisk-den-koldeste-maaned) highlights February as historically cold since 1947, which could potentially influenced biking patterns among Danes. The consistently low bike counts in 2006 appear odd, and upon closer examination of the 2012 data, it becomes apparent that two-thirds of the streets measured from only have data available from June onwards.


Analyzing the overall trends across all years, it is observed that June, August, and September have the highest density of bikes, while the winter months typically have the lowest counts. Additionally, July often exhibits lower counts compared to neighboring months.  This occurrence may be attributed to many Danes vacationing during this month and potentially being away from the city. Moreover, with all schools on summer vacation in July, fewer children may be commuting via bike lanes during this period.


XXXXXX ADD TEXT FOR *RØD TRÅD* XXXXXXXXXX

__NEW HEADER! Comparison (IV)__

XXX Introduction  XXX

<embed 
       type="text/html" 
       src="A3\bokeh_population_spots.html"
       width="1100"
       height="450">
_Figure 3: Trends in population and bike spots in the districts of Copenhagen._

In the interactive plot, the first noticeable feature is the population progress across various districts in Copenhagen. The population data spans from the year 2000 to 2024, with measurements taken quarterly from 2002 to 2024, and once each in 2000 and 2001.
Additionally, is the plot showing the visualization of the cumulative number of bike spots across different districts over the years. The initial value for this cumulative sum is the total number of bike spots without registration dates.

A closer analysis of the plot reveals that while the populations of most districts remain relatively stable over the years, notable increases stand out in _Amager Vest_, _Vesterbro - Kongens Enghave_ and _Valby_. Specifically, these districts have experienced population increases of 42,983, 30,608, and 19,571 respectively.

Focusing on Amager Vest, the corresponding trend in bike spots over time can be plotted. A noticeable increase is observed in bike spots, especially from July 2014 to February 2017. Interestingly, this increasing in bike infrastructure does not directly correlate with the population growth in Amager Vest. \
When examining the data for Vesterbro - Kongens Enghave, the number of bike spots remains relatively stable from 2001 to 2016. However, a significant change occurs in 2017, indicating proactive efforts by the municipality to accommodate the population growth.\
For the final district, Valby, which experienced an increase over the 24 years, an analysis of the trends in bike spots and population can reveal a parallel growth in population and the cumulative number of bike spots. Despite the increase in population, there is no corresponding increase in bike spots.

When plotting the cumulative sums of bike spots across different districts in Copenhagen, a notable increase is observed particularly in the years 2016 and 2017. Specifically, districts such as Indre By saw a significant rise of approximately 12,000 spots, followed by Vesterbro - Kongens Enghave with an increase of about 4,000 spots, and Østerbro with a rise of 2,000 spots. Conversely, districts like Vanløse, Brønshøj - Husum, and Bispebjerg exhibited minimal growth, remaining among the districts with the fewest bike spots.\
Another noteworthy observation is the upward trend that emerged around the year 2001, during which many districts experienced growth as well. This could potentially be attributed to the initiation of the project and the implementation of bike rack and spot counting measures.

As previously mentioned, Indre By witnessed a surge in bike spots during 2016 and 2017. However, upon examining the population progression from 2000 to 2024, the increase appears less significant, with the population rising from 43,691 to 56,668, totaling an increase of almost 13,000 citizens. This trend could be attributed to the growing number of individuals working in Indre By while living outside of Copenhagen. Supporting this notion, the lexicon paper [Indre By](https://trap.lex.dk/Indre_By), notes that while 1/11 of Copenhagen municipality's citizens reside in Indre By, nearly 1/3 of the citizens of the municipality work within the district.

Overall, this plot illustrates the general population trends across districts, the total number of bike spots, and the correlation between population and bike spots. It's evident that both the population and bike spots are on the rise. However, it's important to note that the trend in bike spots represents the registered spots within the period, potentially excluding some spots and overlooking those removed over the years, which could affect the accuracy of the calculations.

__Geographical analysis of bike racks within Copenhagen (V)__\
 Copenhagen is know globally for its cycling culture and presents an ideal casestudy for understanding the dynamics of urban bike trafic. To convince the dayly comuters of Copenhagen to grab their bike in prefrence to a car, when comuting trough the city, it is nessesary that the city offers a sufficient and convinient infrastructure for bike trafic. 

Every cyclist needs a place to securely park their bike upon arriving at their destination. Failure to meet this infrastructure need can lead to a situation where commuters struggle to find available parking spots for their bikes. In rush situations, they may park their bikes purposelessly next to others, obstructing sidewalks or impeding others' access to their bikes. Many commuters are familiar with the frustration of digging their bikes from a pile of abandoned bicycles before staring their comute. The lack of bikeracks dose therby not only creating a messy cityscape but also makes it less atrictive for comuters to use their bike. 

The strategic placement of bike racks serves as a reflection of the city's effort to support cycling as a primary mode of transportation. It is therefore interesting to look at the placement of bikeracks acroos the city to evaluate which current need are prioritised and which districs could use resources to support cycling as a viable transportation option 

<embed 
       type="text/html" 
       src="A3\Geoplot_antal_pladser.html"
       width="1100"
       height="350">
_Figure 4: XXX_

<embed 
       type="text/html" 
       src="A3\Geoplot_antal_pladser_per_m2.html"
       width="1100"
       height="350">
_Figure 5: XXX_

<embed 
       type="text/html" 
       src="A3\Geoplot_antal_pladser_per_befolkning.html"
       width="1100"
       height="350">
_Figure 6: XXX_

The first geoplot (*figure 4*) shows the placement of each registred bikerack as well as the total number of bikespots pr districts. This plot shows that the region Indre By is the district with the most registred bikespots with 26731 bikespots. The outer nordwest districs Valby, Vanløse, Brønshøj-Husum and Bispebjerg all have a number of bikeracks in the range 1500-3000. Looking at the geogorapical placement of each dataplot it can be seen that major roads such as Frederikssundvej, Amagerbrogade and Østerbrograde are traced out as many bikeracks are placed on these streets.


The second geoplot, *figure 5* shows the placement of each registred bikerack as well as the total number of bikespots pr m2 pr districts. This is to showcase the density of the number of bikespots acroos the differet districs. This plots shows that the density of bikeracks are higher in the inner districs compared to the outer districs. The first and the secound geoplot roughly shows the same tendency as most of the districs in copenhagen have rougly the same area. Smaller regions as Nørrebro is rated sligtly better, while larger regions as Amager Vest are rated sligtly worse.

*Figure 6*, third geoplot shows the placement of each registred bikerack as well as the total number of bikespots pr citizen pr districts. The aim of this plot is also to show the density of bikeplots acroos the different districs, but in perspective of the population of the disdrict. It is interesting to see the range of these numbers. In the North-West district of Copenhagen is there only 0.02 bikespots pr citizan, while there is 0.40 bikespots pr citizen in Indre By. This means that bikespots are much more accesable in Indre By compared to the outer districs. 

Overall the three geoplots roughly showcases the same tendencies. The data suggests a significantly higher concentration of bike racks in the inner districts compared to the outer areas. This could be as the inner districts of Copenhagen serve as major employment hubs, attracting a significant influx of commuters on a daily basis. As a result, there is a greater demand for cycling infrastructure in these areas to accommodate the commuting needs of residents and workers.

While the inner districts may naturally attract more attention and investment in terms of bike infrastructure due to higher demand and visibility, efforts should be made to ensure that outer districts receive adequate resources to support cycling as a viable transportation option.


<embed 
       type="text/html" 
       src="A3\Geoplot_density.html"
       width="1100"
       height="350">
_Figure 7: XXX_

*Figure 7* shows the placement of each registred bikerack, where the size and opacity of each dot is corrrelated to the number of spots for the given bikerack, as well as the total number of bikespots pr districts. This is to show the density of bikerakcs across copenhagen and the density of clusteres within the districs. The opacity for each dot is linear to the size. This fuction is choosen such that a cluster of bikeracks nearby eachother is shown more clearly as the opacity for each datapoint is added up. The size of each dot is also a linear fuction of the size. This fuction is choosen to favor larger bikeracks as a bikerack of 240 bikespots physically takes up more space than 2 bikespots.  Here it can be seen that large culsters of bikerakcs are localed at major train and bus stations such as Valby station, Carlsberg station, Hovedbanegården, Nøreport station and Husum station. Looking at districs on Amager, most the major bikeracks are also located along metro stops on the M1 metro line and M2 metro line. This showcases how it is a priority to make it asseciable to connect biketraffic with public transport. This is to support the comuters that travel a longer distance, where they prefere not to bike all the way. This is also to support the many commuters that uses puclic transport to travel to the city or out of the city.

This plot also shows how the dentity of bikerakcs are unevenly distributed within each districs. Lookling at Vesterbro-Kongesn Enghave it can be seen that most bikeracks within this districs are located at Vesterbro which is the part of the districs closest to center of the city. 


<embed 
       type="text/html" 
       src="A3\Geoplot_ownership.html"
       width="1100"
       height="350">
_Figure 8: XXX_

*Figure 8* above shows the placement of each registred bikerack, coloured accordinglig to who own it, as well as the total number of bikespots pr districts. Here it can be seen that many of the public bikeracks are placed along major roads of copenhagen such as Frederikssundvej. This shows that there is a great protential for the state to place more bikeracks more evenly distributed along the districs. 


|         **District**        | **No of spots** | **Public spots** | **Private spots** | **Ratio of public spots** |
|-----------------------------|-----------------|------------------|-------------------|---------------------------|
|         Amager Vest         |       4109      |       2644       |        1073       |           0.6435          |
|          Amager Øst         |       3051      |       1827       |        389        |           0.5988          |
|          Bispebjerg         |       2164      |        840       |        1324       |           0.3882          |
|       Brønshøj - Husum      |       1808      |        959       |        849        |           0.5304          |
|           Nørrebro          |       7354      |       3255       |        4071       |           0.4426          |
|            Valby            |       2806      |       1797       |        979        |           0.6404          |
|           Vanløse           |       1506      |        464       |        1042       |           0.3081          |
| Vesterbro - Kongens Enghave |      10868      |       5208       |        4378       |           0.4792          |
|           Østerbro          |      14059      |       5022       |        7486       |           0.3572          |

_Table 3: XXXXX._

Looking at the keynumber of *table 3* it can be seen that there are very few bikeracks in Vanløse and only 30.8% of the bikespots in Vanløse is owned by the public. Looking at the geoplots it is seen that the density of bike racks pr citizen for Vanløse is very low. It could therby be a posiablility to invest in more bikeracks in this districs to ensure that this districs receive adequate resources to support cycling as a viable transportation option.


__Discussion and Conclusion (VI)__



