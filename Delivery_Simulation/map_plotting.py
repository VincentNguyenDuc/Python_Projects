import city_country_csv_reader
from trip import Trip, create_example_trips
from mpl_toolkits.basemap import Basemap
import numpy as np
from locations import *
import matplotlib.pyplot as plt

def find_lat_long(destination_list: list) -> list:
    """
    This function find upper lat, long and lower lat, long

    Args:
        destination_list (list): _description_

    Returns:
        list: _description_
    """
    # initialize variable to store upper, lower long and lat
    upper_long = -180
    upper_lat = -180
    lower_long = 180
    lower_lat = 180

    # loop through the list of every city within the trip
    for city in destination_list:
        # get lat and long of the city
        city_long = float(city.longitude)
        city_lat = float(city.latitude)

        # find highest lat and long, which will be upper long and upper lat
        if city_long > upper_long:
            upper_long = city_long
        if city_lat > upper_lat:
            upper_lat = city_lat

        # find smallest lat and long, which will be lower long and lower lat
        if city_long < lower_long:
            lower_long = city_long
        if city_lat < lower_lat:
            lower_lat = city_lat
    
    # return the lat and long
    return [upper_long + 5, upper_lat + 5, lower_long - 5, lower_lat - 5]



def plot_trip(trip: Trip, projection = 'cyl', line_width=2, colour='b') -> None:
    """
    Plots a trip on a map and writes it to a file.
    Ensures a size of at least 50 degrees in each direction.
    Ensures the cities are not on the edge of the map by padding by 5 degrees.
    The name of the file is map_city1_city2_city3_..._cityX.png.
    """

    # get a list of every cities within the trip
    destination_list = [trip.departure] + trip.next_city[:]
    length = len(destination_list)

    # create new figure
    plt.figure()

    # setup cyl map projection.

    # calculate longitude and latitude to customize the map
    long_lat = find_lat_long(destination_list)

    upper_long = long_lat[0]
    upper_lat = long_lat[1]

    lower_long = long_lat[2]
    lower_lat = long_lat[3]

    m = Basemap(resolution='i',projection=projection, 
                urcrnrlon=upper_long, urcrnrlat=upper_lat,
                llcrnrlon=lower_long, llcrnrlat=lower_lat)

    m.drawcoastlines()
    m.drawcountries(color='#ffffff', linewidth=0.5)
    m.fillcontinents(color='#c0c0c0', lake_color='#ffffff')
    # draw parallels
    m.drawparallels(np.arange(-90.,120.,30.),labels=[1,0,0,0])
    # draw meridians
    m.drawmeridians(np.arange(0.,420.,60.),labels=[0,0,0,1])


    # plot the trip in the map
    for i in range(length - 1):
        # loop through the list of every city in the trip
        # draw line using great circle 
        depature_lat = float(destination_list[i].latitude)
        depature_long = float(destination_list[i].longitude)

        destination_lat = float(destination_list[i + 1].latitude)
        destination_long = float(destination_list[i + 1].longitude)
        
        m.drawgreatcircle(depature_long, depature_lat, destination_long, destination_lat, linewidth=line_width, color=colour)
    

    # read the map into file
    file_name = "map"
    for city in destination_list:
        file_name += f"_{city.name}"
    file_name += ".png"
    plt.savefig(file_name, format="png")
        

if __name__ == "__main__":
    city_country_csv_reader.create_cities_countries_from_CSV("worldcities_truncated.csv")

    create_example_countries_and_cities()

    trips = create_example_trips()

    for trip in trips:
        plot_trip(trip)