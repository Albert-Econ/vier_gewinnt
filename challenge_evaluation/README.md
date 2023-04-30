Features in the dataset

Neighborhood FID
unique identifyer for all districts of Frankfurt/Main

Land value
Land prices for individual parcel areas have been collected from BORIS-D and provided by the challenge hosts.

treecover, builtup, shrubland, grassland
Using the ESA WorldCover satellite imagery, information on the four classes tree cover, grassland, shrubland and built-up area has been read from the respective TIFF   files for each 10m raster element using QGIS. Within each neighborhood, the number of raster elements with evidence of the class have been counted and set relative     to the total   number of raster elements within the respective neighborhood. This yields features indicating the share of the area in each neighborhood that is covered by trees,     shrubs, grass or built-up structures.
  
affected07, affected25, flugschneise
Frankfurt airport has been ranked the 4th busiest airport in Europe. The airport is located 12km west of downtown Frankfurt. Some neighborhoods are especially         affected by approaching and departing traffic, depending on the direction of the wind and the resulting operating direction (25 - departures towards west, 07 -         arrivals from west). We download the official arrival and departure routes from the airport operator Fraport (https://www.fraport.com/de/umwelt/schallschutz/flugbetrieb--verfahren/flugrouten--verfahren.html) in PDF format. The PDFs are converted to TIFF. TIFFs are then georeferenced using QGIS. We trace the routes using line layers in QGIS and then find the intersection of the routes and neighborhood polygons. We create binary variable that shows neighborhoods affected by departing traffic (affected07), arriving traffic (affected25), or any of the two (flugschneise)

NUM_subway, NUM_railway, NUM_shops, NUM_hospitals, NUM_schools, NUM_parks
Using the OSM API, we directly import and prepare information on subway stations, railway stations, supermarkets, hospitals, schools and parks as examples of aminities in the city. We then count the number of those amenities in each neighborhood. Amenities spanning multiple neighborhoods are counted towards each of the neighborhoods it intersects with.

area
area of the neighborhoods, calculated from polygons.

pop_nbh
population in the neighborhood, calculated from Zensus

gerborn_tot_nbh
number of German born citiziens in the neighborhood, calculated from Zensus

mig_share_nbh
share of migrants in the neighborhood, calculated from Zensus

pop_density
population density in the neighborhood, calculated from Zensus

hh_child_couple_nbh, hh_child_single_nbh, hh_child_single_share_nbh
number of households with couples and children, number of households with a single parent and children, share of households with a single parent and children in the neighborhood, calculated from Zensus

dist
Distance from city centre

build count, house count, apartement count
number of buildings and of houses and apartements especially, from buildings data set, provided by challenge host

resid share
share of buildings with residential use among all buildings, excluding those without a use flag

areatype_agri, areatype_commerce, areatype_mixed
binary variables indicating whether there are areas dedicated to agriculture, commerece or mixed use within each neighborhoods

Neighborhoods
indicating the name of the neighborhoods, for reference
