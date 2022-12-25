from __future__ import annotations 
from enum import Enum
from geopy.distance import great_circle
import math


class CapitalType(Enum):
    """
    The different types of capitals (e.g. "primary").
    """
    primary = "primary"
    admin = "admin"
    minor = "minor"
    unspecified = ""

    def __str__(self) -> str:
        return self.value


class Country():
    """
    Represents a country.
    """

    countries = dict() # a dict that associates country names to instances. 

    def __init__(self, name: str, iso3: str) -> None:
        """
        Creates an instance with a country name and a country ISO code with 3 characters.
        """
        # initialize Country object
        self.name = name
        self.iso3 = iso3
        self.cities_list = []
        self.countries[name] = self

    def _add_city(self, city: City):
        """
        Adds a city to the country.
        """	
        self.cities_list.append(city)


    def get_cities(self, capital_types: list[CapitalType] = None) -> list[City]:
        """
        Returns a list of cities of this country.

        The argument capital_types can be given to specify a subset of the capital types that must be returned.
        Cities that do not correspond to these capital types are not returned.
        If no argument is given, all cities are returned.
        """
        # if no argument is given, copy the whole cities_list
        if capital_types is None:
            return_list = self.cities_list.copy()
        else:
            # if there is capital_type
            return_list = []
            
            # loop through the cities_list
            for city in self.cities_list:
                # get every city that have capital_type, and add to the return_list
                if city.capital_type in capital_types:
                    return_list.append(city)

        # return the list of cities
        return return_list


    def get_city(self, city_name: str) -> City:
        """
        Returns a city of the given name in this country.
        Returns None if there is no city by this name.
        If there are multiple cities of the same name, returns an arbitrary one.
        """
        for city in self.cities_list:
            if city.name == city_name:
                return city

    def __str__(self) -> str:
        """
        Returns the name of the country.
        """
        return str(self.name)


class City():
    """
    Represents a city.
    """

    cities = dict() # a dict that associates city IDs to instances.

    def __init__(self, name: str, latitude: str, longitude: str, country: str, capital_type: str, city_id: str) -> None:
        """
        Initialises a city with the given data.
        """
        # initialize a City Object
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.country = country
        self.capital_type = CapitalType(capital_type)
        self.city_id = city_id
        self.cities[city_id] = self

        # get the country object from the name of the country that the city belongs to
        self.country_obj = Country.countries[self.country]

        # add this city to the Country Object of its own
        self.country_obj._add_city(self)

    def distance(self, other_city: City) -> int:
        """
        Returns the distance in kilometers between two cities using the great circle method,
        rounded up to an integer.
        """
        # get the latitude and longitude of this city
        my_city = (float(self.latitude), float(self.longitude))

        # get the latitude and longitude of the other city
        other = (float(other_city.latitude), float(other_city.longitude))

        # return the distance using great_circle in km
        return math.ceil(great_circle(my_city, other).km)

    def __str__(self) -> str:
        """
        Returns the name of the city and the country ISO3 code in parentheses.
        For example, "Melbourne (AUS)".
        """
        return str(self.name + " ({})".format(self.country_obj.iso3))



def create_example_countries_and_cities() -> None:
    """
    Creates a few Countries and Cities for testing purposes.
    """
    australia = Country("Australia", "AUS")
    melbourne = City("Melbourne", "-37.8136", "144.9631", "Australia", "admin", "1036533631")
    canberra = City("Canberra", "-35.2931", "149.1269", "Australia", "primary", "1036142029")
    sydney = City("Sydney", "-33.865", "151.2094", "Australia", "admin", "1036074917")

    japan = Country ("Japan", "JPN")
    tokyo = City("Tokyo", "35.6839", "139.7744", "Japan", "primary", "1392685764")



def test_example_countries_and_cities() -> None:
    """
    Assuming the correct cities and countries have been created, runs a small test.
    """
    australia = Country.countries['Australia']
    canberra =  australia.get_city("Canberra")
    melbourne = australia.get_city("Melbourne")
    sydney = australia.get_city("Sydney")


    print("The distance between {} and {} is {}km".format(melbourne, sydney, melbourne.distance(sydney)))

    for city in australia.get_cities([CapitalType.admin, CapitalType.primary]):
        print("{} is a {} capital of {}".format(city, city.capital_type, city.country))


if __name__ == "__main__":
    create_example_countries_and_cities()
    test_example_countries_and_cities()