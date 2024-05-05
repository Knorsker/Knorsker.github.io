---
layout: default
---
*Updated: {% assign copenhagen_time = site.time | date: "%d-%m-%Y %H:%M:%S" | date: "%s" | plus: 3600 | date: "%d-%m-%Y %H:%M:%S" %}{{ copenhagen_time }}*


__Introduction (I)__

To get our Notebook click [HERE](A3\Notebook.ipynb)


__Data (II)__\
When analyzing the usage of bikes within Copenhagen, we will be using numerous datasets. The datasets we are using include bike count data, bike stands data, population data, and geoplot data for each of the districts in Copenhagen. All datasets are provided by *opendata.dk*, except for population data, which is gathered from *the City of Copenhagen Statbank*.

The dataset containing bike counts spans 10 different years, from 2005 to 2014. This data is collected by counters placed on different bike roads within Copenhagen city. The number of bike roads counted varies over the years, as shown in *Table 1*, which provides an overview of the number of bike roads the data is collected from. This variation is important to take into account when using the data for analysis.


|Year| 2005 | 2006 | 2007 | 2008 | 2009 | 2010 | 2011 | 2012 | 2013 | 2014 | 
|--------|--------|---------|-----------|----------|--------|----------|--------|--------|--------|--------|
|No. Streets|  4  |   12  | 12      | 12     | 13   | 13     | 13   |12   |13   |9   |

_Table 1: Number of streets, where data is measured from._

Secondly we have the population data, this data contains the population number within each district in Copenhagen over time. We have extracted the quantiles from year 2000 to 2024 to make it possible gain a better understanding of the trends.

Lastly we have the bike racks data. It contains various information about bike racks in Copenhagen, i.a. the number of spots and location of the bike racks. In addition to this dataset, we have utilized the dataset called 'Bydele' from *opendata.dk*, which includes a GeoJSON file over the different districts of Copenhagen.


|     District              | Public | Private | Not registred | Proportion of public |
|--------------------------|--------|---------|---------------|----------------------|
| Amager Vest              | 221    | 119     | 32            | ~59.4%               |
| Amager Øst               | 125    | 48      | 76            | ~50.2%               |
| Bispebjerg               | 45     | 150     | 0             | ~23.1%               |
| Brønshøj-Husum           | 53     | 68      | 0             | ~43.8%               |
| Indre By                 | 864    | 518     | 296           | ~51.5%               |
| Nørrebro                 | 372    | 418     | 4             | ~46.9%               |
| Valby                    | 91     | 111     | 1             | ~44.8%               |
| Vanløse                  | 25     | 75      | 0             | 25.0%                |
| Vesterbro - Kongens Enghave | 456  | 438     | 23            | ~49.7%               |
| Østerbro                 | 506    | 818     | 83            | ~36.0%               |


_Table 2: Amount of public, private and not registred bike racks._


XXXX Referance til tabel 2 mangler, tænker ikke vi skal have det med, hvis ikke vi benytter os af det. XXXX



__Temporal Trends and Seasonal Patterns of bike Activity in Copenhagen (III)__\
The streets of Copenhagen are full of cyclists on a daily basis who use their bikes to and from work, shopping and much more. It is not unusual for the bike racks to be full, and for bikes to stand up from street walls and by lampposts. In this section, we delve into the trends shaping the cycling lifestyle on Copenhagen's streets by looking at the total amount of bikers during the week, the month and the year. 

![One time-series / bar chart](/A3/168hourplot.png)
_Figure 1: A 168 hour barplot showing the patterns for each hour in a week._

XXX Kan vi lave disse blots til 2 forskellige plots af 2x2 og 2x3 eller noget i den stil, synes de er for små til at kunne forklare/aflæse.? XXX

Examining *Figure 1*, a distinct pattern gradually becomes apparent, revealing consistent trends for weekdays across each year. The appearance of two distinct peaks during weekdays are a clear indicator of rush hour periods, marking the busy morning and afternoon hours when the citizens commute to and from work, school, and other engagements, amplifying the cycling activity within the urban landscape. Furthermore, a noticeable decrease in the number of cyclists is observed during the weekends. Additionally, it's visible that more people are out cycling at night on weekends compared to weekdays. This could be because of the city's nightlife and social events.

XXX Noget om forskellen fra år til år i figur 1 XXX

<embed 
       type="text/html" 
       src="A3\Bokeh_monthly.html"
       width="600"
       height="400">
_Figure 2: Monthly bar plot illustrating total number of bikes for each month._

To gain better insight into the biking habits of people in Copenhagen throughout the year, a bar plot is created for each year, see *figure 2*. The plot shows the number of bikes counted in Copenhagen for each month, where it is possible to selcet the desired year in the box beside the plot. 

An analysis of *figure 2* reveals a notable inadequacy in some of the data. For instance, in 2005, there are no recorded bike counts in December. Additionally, an odd number of bike counts from Febuary to May in year 2012, which are notably lower compared to neighboring months and years. Similarly, 2006 exhibits a lower density of bikes in the first five months. For 2010, we see a low number of bikes in the early months.

Several factors may contribute to these variations over the years. For instance in 2012, a [local article](https://www.dr.dk/nyheder/vejret/februar-er-historisk-den-koldeste-maaned) highlights February as historically cold since 1947, which could potentially influenced biking patterns among Danes. XXXXX The consistently low bike counts in 2006 appear odd, and upon closer examination of the 2012 data, it becomes apparent that two-thirds of the streets measured from only have data available from June onwards. (noget med tallene her) XXXXX


Analyzing the overall trends across all years, it is observed that June, August, and September have the highest density of bikes, while the winter months typically have the lowest counts. Additionally, July often exhibits lower counts compared to neighboring months.  This occurrence may be attributed to many Danes vacationing during this month and potentially being away from the city. Moreover, with all schools on summer vacation in July, fewer children may be commuting via bike lanes during this period.

__Trends in population and bike spots (IV)__

As we delve deeper into understanding the dynamics of Copenhagen's cycling culture, it is important to correlate the general bike patterns of the citizens in Copenhagen with the city's developing population and infrastructure development. In line with the variation in the number of bikes across seasons, Copenhagen's population has experienced its own changes. Understanding the interplay between these two facets provides valuable insight into the city's transportation ecosystem. This section will explore the population trends and the availability of bike racks in Copenhagen, shedding light on the relationship between urban demography and cycling infrastructure.

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
 Copenhagen is known globally for its cycling culture and presents an ideal case study for understanding the dynamics of urban bike traffic. To convince the daily commuters of Copenhagen to grab their bike in preference to a car, when commuting through the city, it is necessary that the city offers a sufficient and convenient infrastructure for bike traffic. 

Every cyclist needs a place to securely park their bike upon arriving at their destination. Failure to meet this infrastructure need can lead to a situation where commuters struggle to find available parking spots for their bikes. The lack of bike racks not only creates a messy cityscape but also makes it less attractive for commuters to use their bike. 

The strategic placement of bike racks serves as a reflection of the city's effort to support cycling as a primary mode of transportation. It is therefore interesting to look at the placement of bike racks across the city to evaluate which current needs are prioritised, and which districts could use resources to support cycling as a viable transportation option.

<embed 
       type="text/html" 
       src="A3\Geoplot_antal_pladser.html"
       width="1100"
       height="350">
_Figure 4: A visualization of the number of bike spots in the districts of Copenhagen. The dots represent the exact bike racks around in Copenhagen._

<embed 
       type="text/html" 
       src="A3\Geoplot_antal_pladser_per_m2.html"
       width="1100"
       height="350">
_Figure 5: A visualization of the number of bike spots per m<sup>2</sup> in the districts of Copenhagen. The dots represent the exact bike racks around in Copenhagen._

<embed 
       type="text/html" 
       src="A3\Geoplot_antal_pladser_per_befolkning.html"
       width="1100"
       height="350">
_Figure 6: A visualization of the number of bike spots per citizen in the districts of Copenhagen. The dots represent the exact bike racks around in Copenhagen._

The first geoplot (*figure 4*) shows the placement of each registered bike rack as well as the total number of bike spots per district. This plot shows that the district Indre By is the district with the most registered bikespots with 26731 bikespots. The outer Nordvest districts Valby, Vanløse, Brønshøj-Husum and Bispebjerg all have a number of bike racks in the range 1500-3000, which can also be seen in *figure 3* when plotting the bike spots. Looking at the geographical placement of each data plot it can be seen that major roads such as Frederikssundvej, Amagerbrogade and Østerbrograde are traced out as many bikeracks are placed on these streets.

The second geoplot (*figure 5*) shows the placement of each registered bike rack as well as the total number of bike spots per m<sup>2</sup> per district. This is to showcase the density of the number of bike spots across the different districts. This plot shows that the density of bike racks is higher in the inner districts compared to the outer districts. The first and the second geoplot roughly show the same tendency as most of the districts in Copenhagen have roughly the same area. Smaller regions, such as Nørrebro, are rated slightly better, while larger regions, such as Amager Vest, are rated slightly worse.

The third geoplot (*figure 6*) shows the placement of each registered bike rack as well as the total number of bike spots per citizen per district. The aim of this plot is also to show the density of bike spots across the different districts - though in this case, it is relative to the population of the district. It is interesting to see the range of these numbers. In the Nordvest district of Copenhagen, there are only 0.02 bike spots per citizen, while there are 0.40 bike spots per citizen in Indre By. This means that bike spots are much more accessible in Indre By compared to the outer districts. 

Overall the three geoplots roughly showcase the same tendencies. The data suggests a significantly higher concentration of bike racks in the inner districts compared to the outer areas. This could be because the inner districts of Copenhagen serve as major employment hubs, attracting a significant influx of commuters on a daily basis. As a result, there is a greater demand for cycling infrastructure in these areas to accommodate the commuting needs of residents and workers.

While the inner districts may naturally attract more attention and investment in terms of bike infrastructure due to higher demand and visibility, efforts should be made to ensure that outer districts receive adequate resources to support cycling as a viable transportation option.


<embed 
       type="text/html" 
       src="A3\Geoplot_density.html"
       width="1100"
       height="350">
_Figure 7: A geoplot of the number of bike spots in the districts of Copenhagen. The markers visualize the amount of bike spots for the located bike rack._

*Figure 7* shows the placement of each registered bike rack, where the size and opacity of each dot are correlated to the number of spots for the given bike rack, as well as the total number of bike spots per district. This is to show the density of bike racks across Copenhagen and the density of clusters within the districts. The opacity for each dot is linear to the size. This function is chosen such that a cluster of bike racks close to each other is shown more clearly as the opacity for each data point is added up. The size of each dot is also a linear function of the size. This function is chosen to favour larger bike racks as a bike rack of 240 bike spots physically takes up more space than that of 2 bike spots.  Here it can be seen that large clusters of bike racks are located at major train and bus stations such as Valby Station, Carlsberg Station, Hovedbanegården, Nøreport Station and Husum Station. Looking at districts on Amager, most of the major bike racks are also located along metro stops on the M1 metro line and M2 metro line. This showcases how it is a priority to make it accessible to connect bike traffic with public transport. This is to support the commuters that travel a longer distance, where they prefer not to bike all the way. This is also to support the many commuters that use public transport to travel to the city or out of the city.

This plot also shows how the density of bike racks is unevenly distributed within each district. Looking at Vesterbro-Kongens Enghave it can be seen that most bike racks within this district are located at Vesterbro which is the part of the district closest to the center of the city. 

<embed 
       type="text/html" 
       src="A3\Geoplot_ownership.html"
       width="1100"
       height="350">
_Figure 8: A geoplot of the number of bike spots in the districts of Copenhagen. The markers visualize the location af the bike racks coloured according to the ownership._

*Figure 8* shows the placement of each registered bike rack, coloured according to who owns it, as well as the total number of bike spots per district. Here it can be seen that many of the public bike racks are placed along the major roads of Copenhagen such as Frederikssundvej. This shows that there is great potential for the government to place more bike racks more evenly distributed along the districts. Moreover, it can be seen that a lot of the private bike racks are located at Østerbro and Nørrebro, while a lot of the public bike racks are placed in Indre By and Vesterbro.

|         **District**        | **No of spots** | **Public spots** | **Private spots** | **Ratio of public spots** |
|-----------------------------|-----------------|------------------|-------------------|---------------------------|
|         Amager Vest         |       4109      |       2644       |        1073       |           0.6435          |
|          Amager Øst         |       3051      |       1827       |        389        |           0.5988          |
|          Bispebjerg         |       2164      |        840       |        1324       |           0.3882          |
|       Brønshøj - Husum      |       1808      |        959       |        849        |           0.5304          |
| Indre By                    |       26731     |     13269        |        6663       |           0.4964          |
|           Nørrebro          |       7354      |       3255       |        4071       |           0.4426          |
|            Valby            |       2806      |       1797       |        979        |           0.6404          |
|           Vanløse           |       1506      |        464       |        1042       |           0.3081          |
| Vesterbro - Kongens Enghave |      10868      |       5208       |        4378       |           0.4792          |
|           Østerbro          |      14059      |       5022       |        7486       |           0.3572          |

_Table 3: XXXXX._

Looking at the key numbers of *table 3* it can be seen that there are very few bike racks in Vanløse and only 30.8% of the bikespots in Vanløse are owned by the public. Looking at the geoplots it is seen that the density of bike racks per citizen for Vanløse is very low. It could thereby be a possibility to invest in more bike racks in this district to ensure that this district receives adequate resources to support cycling as a viable transportation option. Furthermore, it can also be seen that the ratio of publiv spots in Bispebjerg and Østerbro are also low, which was also visible in *figure 8*. 


__Discussion and Conclusion (VI)__

