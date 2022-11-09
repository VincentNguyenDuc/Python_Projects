from vehicles import Vehicle, CrappyCrepeCar, DiplomacyDonutDinghy, TeleportingTarteTrolley
from vehicles import create_example_vehicles
from locations import City, Country
from locations import create_example_countries_and_cities
import math


class Trip():
    """
    Represents a sequence of cities.
    """

    def __init__(self, departure: City) -> None:
        """
        Initialises a Trip with a departure city.
        """
        self.departure = departure
        self.next_city = []

    def add_next_city(self, city: City) -> None:
        """
        Adds the next city to this trip.
        """
        self.next_city.append(city)

    def total_travel_time(self, vehicle: Vehicle) -> float:
        """
        Returns a travel duration for the entire trip for a given vehicle.
        Returns math.inf if any leg (i.e. part) of the trip is not possible.
        """
        # copy the list of next_city into dest_list
        dest_list = self.next_city.copy()

        # add the departure to the first position in the list
        dest_list.insert(0, self.departure)

        # calculate total travel time
        total_travel_time = 0

        # loop through the list of destination, not including the last city
        for i in range(len(dest_list) - 1):

            # calculate the travel time between 2 city
            travel_time = vehicle.compute_travel_time(dest_list[i], dest_list[i + 1])

            # if inf then return inf
            if travel_time == math.inf:
                return math.inf
            else:
                total_travel_time += travel_time
        return total_travel_time


    def find_fastest_vehicle(self, vehicles: list[Vehicle]):
        """
        Returns the Vehicle for which this trip is fastest, and the duration of the trip.
        If there is a tie, return the first vehicle in the list.
        If the trip is not possible for any of the vehicle, return (None, math.inf).
        """
        inf_count = 0
        time_min = 1000000000

        # loop through the list of vehicles
        for vehicle in vehicles:
            # calculate the duration
            duration = self.total_travel_time(vehicle)

            # if the vehicle cannot do the trip
            if duration == math.inf:
                # count the number of not possible vehicles
                inf_count += 1
                continue
            else:
                # else then update the fastest time duration
                if duration < time_min:
                    time_min = duration
        
        # if the number of not possible vehicle equals to the number of vehicles
        if inf_count == len(vehicles):
            return tuple([None, math.inf])
        else:
            # else find the fastest vehicle
            for vehicle in vehicles:
                if self.total_travel_time(vehicle) == time_min:
                    return tuple([vehicle, time_min])



    def __str__(self) -> str:
        """
        Returns a representation of the trip as a sequence of cities:
        City1 -> City2 -> City3 -> ... -> CityX
        """
        # get the departure city
        display = str(self.departure)
        # add each next city
        for city in self.next_city:
            display += " -> {}".format(city)
        return str(display)


def create_example_trips() -> list[Trip]:
    """
    Creates examples of trips.
    """

    #first we create the cities and countries
    create_example_countries_and_cities()

    australia = Country.countries["Australia"]
    melbourne = australia.get_city("Melbourne")
    sydney = australia.get_city("Sydney")
    canberra = australia.get_city("Canberra")
    japan = Country.countries["Japan"]
    tokyo = japan.get_city("Tokyo")

    #then we create trips
    trips = []

    for cities in [(melbourne, sydney), (canberra, tokyo), (melbourne, canberra, tokyo), (canberra, melbourne, tokyo)]:
        trip = Trip(cities[0])
        for city in cities[1:]:
            trip.add_next_city(city)

        trips.append(trip)

    return trips


if __name__ == "__main__":
    vehicles = create_example_vehicles()
    trips = create_example_trips()

    for trip in trips:
        vehicle, duration = trip.find_fastest_vehicle(vehicles)
        print("The trip {} will take {} hours with {}".format(trip, duration, vehicle))



