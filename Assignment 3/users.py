from locations import Country, City
from city_country_csv_reader import create_cities_countries_from_CSV

from vehicles import CrappyCrepeCar, DiplomacyDonutDinghy, TeleportingTarteTrolley

from trip import Trip

from get_input import int_input, float_input

from information import background_information, custom_vehicles_information, example_vehicles_information, example_trip_information, countries_name

from prettytable import PrettyTable, ALL




class User():

    # some text art to display
    invalid = """
█ █▄ █ █ █ ▄▀█ █   █ █▀▄ █   █▀█ █   █▀▀ ▄▀█ █▀ █▀▀   ▀█▀ █▀█ █▄█   ▄▀█ █▀▀ ▄▀█ █ █▄ █ █
█ █ ▀█ ▀▄▀ █▀█ █▄▄ █ █▄▀ ▄   █▀▀ █▄▄ ██▄ █▀█ ▄█ ██▄    █  █▀▄  █    █▀█ █▄█ █▀█ █ █ ▀█ ▄
"""
    different_cities = """
█▀█ █   █▀▀ ▄▀█ █▀ █▀▀   █▀▀ █ █ █▀█ █▀█ █▀ █▀▀   ▀█   █▀▄ █ █▀▀ █▀▀ █▀▀ █▀█ █▀▀ █▄ █ ▀█▀   █▀▀ █ ▀█▀ █ █▀▀ █▀ █
█▀▀ █▄▄ ██▄ █▀█ ▄█ ██▄   █▄▄ █▀█ █▄█ █▄█ ▄█ ██▄   █▄   █▄▀ █ █▀  █▀  ██▄ █▀▄ ██▄ █ ▀█  █    █▄▄ █  █  █ ██▄ ▄█ ▄    
"""
    next_step = """
▀█▀ █ █ ▄▀█ █▄ █ █▄▀   █▄█ █▀█ █ █ █   █   █▀▀ ▀█▀ ▀ █▀   █▀▄▀█ █▀█ █ █ █▀▀   █▀█ █▄ █   ▀█▀ █▀█   ▀█▀ █ █ █▀▀   █▄ █ █▀▀ ▀▄▀ ▀█▀   █▀ ▀█▀ █▀▀ █▀█
 █  █▀█ █▀█ █ ▀█ █ █    █  █▄█ █▄█ ▄   █▄▄ ██▄  █    ▄█   █ ▀ █ █▄█ ▀▄▀ ██▄   █▄█ █ ▀█    █  █▄█    █  █▀█ ██▄   █ ▀█ ██▄ █ █  █    ▄█  █  ██▄ █▀▀
"""
    no_problem = """
█▀█ █▄▀ ▄▀█ █▄█   █▄ █ █▀█   █▀█ █▀█ █▀█ █▄▄ █   █▀▀ █▀▄▀█ █
█▄█ █ █ █▀█  █    █ ▀█ █▄█   █▀▀ █▀▄ █▄█ █▄█ █▄▄ ██▄ █░▀░█ ▄
"""
    step_1 = """
█▀▀▀█ ▀▀█▀▀  █▀▀▀  █▀▀█ 　 ▄█  ▄ 　  █▀▀█  █▀▀█  █▀▀▀  █▀▀█ ▀▀█▀▀ ▀█▀  █▄  █  █▀▀█ 　  █   █  █▀▀▀█  █  █  █▀▀█ 　  █▀▀▀  █     █▀▀▀  █▀▀▀ ▀▀█▀▀ 
▀▀▀▄▄   █    █▀▀▀  █▄▄█ 　  █    　  █     █▄▄▀  █▀▀▀  █▄▄█   █    █   █ █ █  █ ▄▄ 　  █▄▄▄█  █   █  █  █  █▄▄▀ 　  █▀▀▀  █     █▀▀▀  █▀▀▀   █ 
█▄▄▄█   █    █▄▄▄  █    　 ▄█▄ ▀ 　  █▄▄█  █  █  █▄▄▄  █  █   █   ▄█▄  █  ▀█  █▄▄█ 　    █    █▄▄▄█  ▀▄▄▀  █  █ 　  █     █▄▄█  █▄▄▄  █▄▄▄   █ 
"""
    step_2 = """
█▀▀▀█ ▀▀█▀▀  █▀▀▀  █▀▀█ 　 █▀█ ▄ 　  █▀▀█  █▀▀█  █▀▀▀  █▀▀█ ▀▀█▀▀ ▀█▀  █▄  █  █▀▀█ 　  █   █  █▀▀▀█  █  █  █▀▀█ 　 ▀▀█▀▀  █▀▀█ ▀█▀  █▀▀█ 
▀▀▀▄▄   █    █▀▀▀  █▄▄█ 　  ▄▀   　  █     █▄▄▀  █▀▀▀  █▄▄█   █    █   █ █ █  █ ▄▄ 　  █▄▄▄█  █   █  █  █  █▄▄▀ 　   █    █▄▄▀  █   █▄▄█ 
█▄▄▄█   █    █▄▄▄  █    　 █▄▄ ▀ 　  █▄▄█  █  █  █▄▄▄  █  █   █   ▄█▄  █  ▀█  █▄▄█ 　    █    █▄▄▄█  ▀▄▄▀  █  █ 　   █    █  █ ▄█▄  █
"""
    step_3 = """
█▀▀▀█ ▀▀█▀▀  █▀▀▀  █▀▀█ 　 █▀▀█ ▄ 　   █▀▀█  █     █▀▀▀█ ▀▀█▀▀ ▀█▀  █▄  █  █▀▀█ 　  █   █  █▀▀▀█  █  █  █▀▀█ 　 ▀▀█▀▀  █▀▀█ ▀█▀  █▀▀█ 
▀▀▀▄▄   █    █▀▀▀  █▄▄█ 　   ▀▄   　   █▄▄█  █     █   █   █    █   █ █ █  █ ▄▄ 　  █▄▄▄█  █   █  █  █  █▄▄▀ 　   █    █▄▄▀  █   █▄▄█ 
█▄▄▄█   █    █▄▄▄  █░   　 █▄▄█ ▀ 　   █     █▄▄█  █▄▄▄█   █   ▄█▄  █  ▀█  █▄▄█ 　    █    █▄▄▄█  ▀▄▄▀  █  █ 　   █    █  █ ▄█▄  █
"""
    step_4 = """
█▀▀▀█ ▀▀█▀▀  █▀▀▀  █▀▀█ 　  █▀█  ▄ 　  █▀▀█  █  █  █▄  █  █▄  █ ▀█▀  █▄  █  █▀▀█ 　  █▀▀▀█ ▀█▀  █▀▄▀█  █  █  █     █▀▀█ ▀▀█▀▀ ▀█▀  █▀▀▀█  █▄  █   
▀▀▀▄▄   █    █▀▀▀  █▄▄█ 　 █▄▄█▄   　  █▄▄▀  █  █  █ █ █  █ █ █  █   █ █ █  █ ▄▄ 　  ▀▀▀▄▄  █   █ █ █  █  █  █     █▄▄█   █    █   █   █  █ █ █    
█▄▄▄█   █    █▄▄▄  █    　    █  ▀ 　  █  █  ▀▄▄▀  █  ▀█  █  ▀█ ▄█▄  █  ▀█  █▄▄█ 　  █▄▄▄█ ▄█▄  █   █  ▀▄▄▀  █▄▄█  █  █   █   ▄█▄  █▄▄▄█  █  ▀█ 
"""
    seperator = "---------------------------------------------------------------------------------------------------------------------------------"

    unavailable = """
█ █ █▄ █ ▄▀█ █ █ ▄▀█ █ █   ▄▀█ █▄▄ █   █▀▀   █▄ █ ▄▀█ █▀▄▀█ █▀▀ █
█▄█ █ ▀█ █▀█ ▀▄▀ █▀█ █ █▄▄ █▀█ █▄█ █▄▄ ██▄   █ ▀█ █▀█ █ ▀ █ ██▄ ▄
"""

    vehicle_set = """
█ █ █ █▀▀   █ █ ▄▀█ █ █ █▀▀   █▀   █▀ █▀▀ ▀█▀ █▀   █▀█ █▀▀   █ █ █▀▀ █ █ █ █▀▀ █   █▀▀ █▀ ▀
▀▄▀▄▀ ██▄   █▀█ █▀█ ▀▄▀ ██▄   ▄█   ▄█ ██▄  █  ▄█   █▄█ █▀    ▀▄▀ ██▄ █▀█ █ █▄▄ █▄▄ ██▄ ▄█ ▄
"""

    speed_invalid = """
▀█▀ █ █ █▀▀   █▀ █▀█ █▀▀ █▀▀ █▀▄   █▄▄ █▀▀ ▀█▀ █ █ █ █▀▀ █▀▀ █▄ █   ▀█   █▀▀ █▀█ █ █ █▄ █ ▀█▀ █▀█ █ █▀▀ █▀   █▀▄▀█ █ █ █▀ ▀█▀   █▄▄ █▀▀   █   ▄▀█ █▀█ █▀▀ █▀▀ █▀█ █
 █  █▀█ ██▄   ▄█ █▀▀ ██▄ ██▄ █▄▀   █▄█ ██▄  █  ▀▄▀▄▀ ██▄ ██▄ █ ▀█   █▄   █▄▄ █▄█ █▄█ █ ▀█  █  █▀▄ █ ██▄ ▄█   █ ▀ █ █▄█ ▄█  █    █▄█ ██▄   █▄▄ █▀█ █▀▄ █▄█ ██▄ █▀▄ ▄
"""

    departure_art = """
█▀▄ █▀▀ █▀█ ▄▀█ █▀█ ▀█▀ █ █ █▀█ █▀▀ ▀
█▄▀ ██▄ █▀▀ █▀█ █▀▄  █  █▄█ █▀▄ ██▄ ▄
"""

    destination_art = """
█▀▄ █▀▀ █▀ ▀█▀ █ █▄ █ ▄▀█ ▀█▀ █ █▀█ █▄ █ ▀
█▄▀ ██▄ ▄█  █  █ █ ▀█ █▀█  █  █ █▄█ █ ▀█ ▄
"""
    enter_art = """
█▀█ █▀█ █▀▀ █▀ █▀   █▀▀ █▄░█ ▀█▀ █▀▀ █▀█   ▀█▀ █▀█   █▀▀ █▀█ █▄░█ ▀█▀ █ █▄░█ █░█ █▀▀
█▀▀ █▀▄ ██▄ ▄█ ▄█   ██▄ █░▀█ ░█░ ██▄ █▀▄   ░█░ █▄█   █▄▄ █▄█ █░▀█ ░█░ █ █░▀█ █▄█ ██▄
"""

    def __init__(self) -> None:
        """
        This method initialize an User object with their name, whether they want choose from example vehicles and trips or create their custom vehicles and trips
        """
        # get user name
        self.name = input("Please enter your name: ")

        # print out background information
        background_information(self.name)

        # press enter to continue
        enter = input(self.enter_art)

        # initialize some variables
        self.vehicles = []
        self.trips = []

        # initialize some variable to store reference of the user
        self.vehicles_refernce = -1
        self.trips_refernce = -1


        self.user_choices()


    def example_vehicles(self):
        """
        This method simply creates example vehicles for the users to choose from
        """
        # print some background information
        example_vehicles_information()

        # create base attribute of objects for each type of vehicle
        base_car = 200
        base_dinghy = [100, 500]
        base_trolley = [3, 2000]


        example_vehicles = []
        print("")
        print(self.vehicle_set)

        # create a table to display vehicles
        vehicle_table = PrettyTable(border=True, header=False)
        vehicle_table.hrules = ALL

        # create 5 example fleets
        for i in range(5):

            # initialize vehicles
            crepe_car = CrappyCrepeCar(base_car)
            donut_dinghy = DiplomacyDonutDinghy(base_dinghy[0], base_dinghy[1])
            tarte_trolley = TeleportingTarteTrolley(base_trolley[0], base_trolley[1])

            # show vehicles to the user
            vehicle_table.add_row([i + 1, crepe_car, donut_dinghy, tarte_trolley])
            example_vehicles.append(tuple([crepe_car, donut_dinghy, tarte_trolley]))

            # increment parameters to create new vehicles in the next loop
            base_car += 50

            base_dinghy[0] += 50
            base_dinghy[1] += 50

            base_trolley[0] += 0.5
            base_trolley[1] += 500

        print(vehicle_table)

        print("")

        condition = False
        while condition is False:

            # let the user choose their fleet
            user_fleet_index = int_input(prompt="Please choose your fleet (1 -> 5): ", restricted_to=[1, 2, 3, 4, 5]) 

            # get the fleet
            user_fleet = example_vehicles[user_fleet_index - 1]

            # print successful line
            print(f"You have successfully chosen fleet {user_fleet_index}!\n")

            # ask if the user want to choose again or not
            user_choice = int_input("Do you want to change your choice? (0 for NO / 1 for YES): ", restricted_to=[0, 1])

            if user_choice == 0:
                condition = True
                print(self.next_step)
            else:
                print(self.no_problem)
        
        self.vehicles = list(user_fleet)

    
    def custom_vehicles(self):
        """
        This method let the users choose their own vehicles with custom parameters
        """
        # print out the vehicle information
        custom_vehicles_information()

        condition = False
        while condition is False:

            # get the number of vehicles that user want
            number_of_vehicles = int_input(prompt="Please enter the number of vehicles that you want: ", positive=True)
            vehicle_list = []

            # get vehicle type, custom parameters
            for i in range(number_of_vehicles):

                # get the type of vehicle
                vehicle_type = int_input(prompt="""Please choose the vehicle type (1 -> 3):
            1. Crappy Crepe Car 
            2. Diplomacy Donut Dinghy
            3. Teleporting Tarte Trolley
Input (1 -> 3): """, restricted_to=[1, 2, 3])
                
                # initialize vehicle
                if vehicle_type == 1:
                    # get parameter
                    speed = float_input(prompt="Please choose the speed of Crappy Crepe Car (km/h): ", positive=True)

                    # initialize vehicle
                    vehicle = CrappyCrepeCar(speed)

                elif vehicle_type == 2:
                    
                    # get parameter
                    while True:
                        within_country_speed = float_input(prompt="Please choose the speed between cities of the same country of Diplomacy Donut Dinghy (km/h): ", positive=True)
                        between_countries_speed = float_input(prompt="Please choose the speed between different countries of Diplomacy Donut Dinghy (km/h): ", positive=True)

                        # the speed between different countries is faster than the speed within country
                        if between_countries_speed <= within_country_speed:
                            print(self.invalid)
                            print(self.speed_invalid)
                            continue
                        else:
                            break
                    
                    # initialize vehicle
                    vehicle = DiplomacyDonutDinghy(within_country_speed, between_countries_speed)
                
                else:
                    # get parameter
                    execution_time = float_input(prompt="Please choose the execution time (h): ", positive=True)
                    distance = float_input(prompt="Please enter the distance (km): ", positive=True)
                    
                    # initialize vehicle
                    vehicle = TeleportingTarteTrolley(execution_time, distance)

                # add vehicle to vehicles list of user
                vehicle_list.append(vehicle)
                

                print(f"We have add {vehicle} to your fleet!\n")

            print("Congratulations! You have created your own fleet:")
            for vehicle in vehicle_list:
                print(f"- {vehicle}")

            # ask if the user want to choose again or not
            print("")
            user_choice = int_input("Do you want to change your choice? (0 for NO / 1 for YES): ", restricted_to=[0, 1])

            if user_choice == 0:
                print(self.next_step)
                self.vehicles = vehicle_list
                condition = True
            else:
                print(self.no_problem)

    def create_countries_and_cities(self):
        """
        This method get the countries: 
        - Initialize 6 countries in 6 different continents
            + Australia (Australia)
            + Vietnam (Asia)
            + France (Europe)
            + USA (North America)
            + Brazil (South America)  
            + Nigeria (Africa)
        - Initialize 2 cities within each country
        """

        country_city_dict = {}

        australia = Country.countries["Australia"]
        melbourne = australia.get_city("Melbourne")
        sydney = australia.get_city("Sydney")

        country_city_dict[australia] = [melbourne, sydney]

        vietnam = Country.countries["Vietnam"]
        hanoi = vietnam.get_city("Hanoi")
        ho_chi_minh = vietnam.get_city("Ho Chi Minh City")

        country_city_dict[vietnam] = [hanoi, ho_chi_minh]

        france = Country.countries["France"]
        paris = france.get_city("Paris")
        marseille = france.get_city("Marseille")

        country_city_dict[france] = [paris, marseille]

        usa = Country.countries["United States"]
        new_york = usa.get_city("New York")
        richmond = usa.get_city("Richmond")

        country_city_dict[usa] = [new_york, richmond]
        
        brazil = Country.countries["Brazil"]
        sao_paulo = brazil.get_city("Sao Paulo")
        rio_de_janeiro = brazil.get_city("Rio de Janeiro")

        country_city_dict[brazil] = [sao_paulo, rio_de_janeiro]

        nigeria = Country.countries["Nigeria"]
        lagos = nigeria.get_city("Lagos")
        kano = nigeria.get_city("Kano")

        country_city_dict[nigeria] = [lagos, kano]

        return country_city_dict


    def getting_city(self):
        """
        This method get the user input of city
        """
        country_city_dict = self.create_countries_and_cities()

        # let the user choose the country
        country_index = int_input(prompt="""Please choose the country
        1. Australia
        2. Vietnam
        3. France
        4. United States
        5. Brazil
        6. Nigeria
Input (1 -> 6): """, restricted_to=[1, 2, 3, 4, 5, 6])

        country = list(country_city_dict.keys())[country_index - 1]

        print(f"You have chosen {country}")

        # let the user choose the city within the chosen country
        cities = list(country_city_dict.values())[country_index - 1]
        city_index = int_input(prompt=f"""Please choose the city
        1. {cities[0]}
        2. {cities[1]}
Input (1 -> 2): """, restricted_to=[1, 2])

        city = cities[city_index - 1]

        return city



    def example_trips(self):
        """
        This method simply creates example trips for the users to choose from
            - Let the user choose the country of departure -> the city of departure
            - Let the user choose the country of destination -> the city of destination 
        """
        example_trip_information()

        condition = False
        while condition is False:

            # getting departure city
            print(self.departure_art)
            departure = self.getting_city()
            print(f"You have chosen {departure} as your departure!\n")

            # getting destination city
            print(self.destination_art)
            destination = self.getting_city()
            print(f"You haver chosen {destination} as your destination!\n")

            # destination and departure must be 2 different cities
            if destination.name == departure.name:
                print(self.invalid)
                print(self.different_cities)
                continue

            # creating trip
            user_trip = Trip(departure)
            user_trip.add_next_city(destination)
            print(f"Congratulations! You have got your departure and destination: {user_trip}")

            # ask if the user want to choose again or not
            user_choice = int_input("Do you want to change your choices? (0 for NO / 1 for YES): ", restricted_to=[0, 1])

            if user_choice == 0:
                print(self.next_step)
                self.trips = user_trip
                condition = True
            else:
                print(self.no_problem)
                self.trips = []


    def getting_country_name(self):
        """
        Check if the country name that user input is available in the countries list

        Args:
            country_name (_type_): name of a country

        Returns:
            _type_: - Country object / Boolean
        """

        while True:
            # let the user input the name of the country
            country_name = input("Please enter the country's name: ")

            # check if the input name is available
            for country in Country.countries.values():
                if country_name.lower() == country.name.lower():
                    return country

            # if not print invalid 
            print(self.invalid)
            print(self.unavailable)      


    def getting_city_name(self, country: Country) -> City:
        """
        Print out the name of every cities belonging to this country using PrettyTable module
        """      
        # create a table to display name of cities
        display_table = PrettyTable(border=True, header=False)
        display_table.hrules = ALL


        city_list = []
        print("")

        # print the cities within the country
        print(f"{country} has the following cities:")

        # number of cities within the country
        length = len(country.cities_list)

        # loop through the list of cities
        for city in country.cities_list:

            # append to the city_list
            city_list.append(city.name)
            
            # if the number of the cities in the country is smaller than 8
            if length < 8:
                if len(city_list) == length:
                    display_table.add_row(city_list)
            
            # else then each row of the table will have 8 cities
            else:
                if len(city_list) == 8:
                    display_table.add_row(city_list)
                    city_list = []
        print(display_table)

        print("")

        # let the user add the city to the trip
        while True:
            city_name = input("Please enter the city that you want to add, note that you have to input the name as shown in the table: ")
            # check if the user input is available
            for city in country.cities_list:
                if city.name == city_name:
                    print(f"We have added {city.name} into your trip!\n")
                    return city

            # if not print invalid and move to the next loop
            print(self.invalid)

                    
                
    def custom_trips(self):
        """
        This method let the users choose their own trips by manually adding all cities
            - Get the number of cities
            - Get the country of departure -> get the city -> get the next country -> get the city 
        """

        print("")
        condition = False
        
        while condition is False:

            trip = []

            # getting the number of cities
            while True:
                number_of_cities = int_input("Please enter the number of cities that you want to add into your trip: ", positive=True)
                print("")
                if number_of_cities > 1:
                    break
                else:
                    print(self.invalid)
            
            # display the name of every countries if the user want to see
            countries_name()

            # getting the cities
            while number_of_cities > 0:
                # get country name
                country = self.getting_country_name()
                # get city name
                city = self.getting_city_name(country)

                # check valid city name
                if len(trip) >= 1 and trip[-1].name == city.name:
                    print(self.invalid)
                    print(self.different_cities)
                    continue
                else:
                    trip.append(city)
                    number_of_cities -= 1
                

            # creating trip
            user_trip = Trip(trip[0])     
            for city in trip[1:]:
                user_trip.add_next_city(city)    
            print(f"Congratulations! You have created your trip: {user_trip}\n")       


            # ask if the user want to choose again or not
            user_choice = int_input("\nDo you want to change your choices? (0 for NO / 1 for YES): ", restricted_to=[0, 1])

            if user_choice == 0:
                print(self.next_step)
                self.trips = user_trip
                condition = True
            else:
                print(self.no_problem)
                self.trips = []


    def user_choices(self):
        """
        This method get the choices from user
        """

        """create vehicles""" 

        # print some text art
        print(self.seperator)
        print(self.step_1)

        # get the reference from the user if the user want to get fleet from examples or create his/her own vehicles fleet
        self.vehicles_refernce = int_input(prompt="How do you want to create your own fleet? (0 for example/ 1 for custom): ", restricted_to=[0, 1])
        if self.vehicles_refernce == 0:
            self.example_vehicles()
        else:
            self.custom_vehicles()

        # print text art
        print(self.seperator)

        # press enter to continue
        enter = input(self.enter_art)

        """create trip"""

        # print some text art
        print(self.seperator)
        print(self.step_2)

        # read csv file
        create_cities_countries_from_CSV("worldcities_truncated.csv")

        # get the reference from the user if the user want to choose from examples trips or create his/her own trips
        self.trips_refernce = int_input(prompt="How do you want to create your own trip? (0 for example/ 1 for custom): ", restricted_to=[0, 1])
        if self.trips_refernce == 0:
            self.example_trips()
        else:
            self.custom_trips()

        # print text art
        print(self.seperator)
        
        # press enter to continue
        enter = input(self.enter_art)
        

if __name__ == "__main__":
    user = User()

