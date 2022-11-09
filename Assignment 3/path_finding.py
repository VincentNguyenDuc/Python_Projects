import city_country_csv_reader
from locations import City, Country
from trip import Trip
from vehicles import Vehicle, create_example_vehicles
import networkx as nx
import math



def find_shortest_path(vehicle: Vehicle, from_city: City, to_city: City) -> Trip:
    """
    Returns a shortest path between two cities for a given vehicle,
    or None if there is no path.
    """
    G = nx.Graph()                              # generate a graph
    G.add_nodes_from(City.cities.values())      # add every cities in the world as nodes
    nodes_list = list(G.nodes)                  # create a list of nodes
    number_of_nodes = G.number_of_nodes()       # the number of nodes
 

    """Adding edges if the distance is not inf"""
    # loop through the number of nodes
    for i in range(number_of_nodes - 1):
        # from a node, loop through every node behind this current node
        for j in range(i + 1, number_of_nodes):

            # calculate weight, which is the travel time
            weight = vehicle.compute_travel_time(nodes_list[i], nodes_list[j])

            # if weight is not inf, then add_edge
            if weight != math.inf:
                G.add_edge(nodes_list[i], nodes_list[j], weight=weight)


    """Find shortest path and return as Trip object"""

    # if there is a path
    if nx.has_path(G, from_city, to_city) is True:

        # calculate the shortest_path
        shortest_path = nx.shortest_path(G, from_city, to_city)

        # get the first city in the path, this will be the departure of the trip
        shortest_trip = Trip(shortest_path[0])
        # add next city
        for city in shortest_path[1:]:
            shortest_trip.add_next_city(city)
        # return the trip
        return shortest_trip


if __name__ == "__main__":
    city_country_csv_reader.create_cities_countries_from_CSV("worldcities_truncated.csv")

    vehicles = create_example_vehicles()

    australia = Country.countries["Australia"]
    melbourne = australia.get_city("Melbourne")
    japan = Country.countries["Japan"]
    tokyo = japan.get_city("Tokyo")
    canberra = australia.get_city("Canberra")

    japan = Country.countries["Japan"]
    tokyo = japan.get_city("Tokyo")



    for vehicle in vehicles:
        print("The shortest path for {} from {} to {} is {}".format(vehicle, melbourne, tokyo, find_shortest_path(vehicle, melbourne, tokyo)))