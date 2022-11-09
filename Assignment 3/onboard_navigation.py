from get_input import int_input
from vehicles import Vehicle
from trip import Trip
from path_finding import find_shortest_path
from map_plotting import plot_trip
from users import User
from prettytable import PrettyTable, ALL
from copy import copy
from information import navigation_information
from alive_progress import alive_bar
import time


class Navigation():

    # some text art for display
    fleet_display = """
█─█─█▄─▄▄─█▄─▄▄▀█▄─▄▄─███▄─▄█─▄▄▄▄███▄─█─▄█─▄▄─█▄─██─▄█▄─▄▄▀███▄─▄▄─█▄─▄███▄─▄▄─█▄─▄▄─█─▄─▄─█
█─▄─██─▄█▀██─▄─▄██─▄█▀████─██▄▄▄▄─████▄─▄██─██─██─██─███─▄─▄████─▄████─██▀██─▄█▀██─▄█▀███─███
▀▄▀▄▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▀▀▄▄▄▀▄▄▄▄▄▀▀▀▀▄▄▄▀▀▄▄▄▄▀▀▄▄▄▄▀▀▄▄▀▄▄▀▀▀▄▄▄▀▀▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▀▄▄▄▀▀
"""
    trip_display = """
█─█─█▄─▄▄─█▄─▄▄▀█▄─▄▄─███▄─▄█─▄▄▄▄███▄─█─▄█─▄▄─█▄─██─▄█▄─▄▄▀███─▄─▄─█▄─▄▄▀█▄─▄█▄─▄▄─█
█─▄─██─▄█▀██─▄─▄██─▄█▀████─██▄▄▄▄─████▄─▄██─██─██─██─███─▄─▄█████─████─▄─▄██─███─▄▄▄█
▀▄▀▄▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▀▀▄▄▄▀▄▄▄▄▄▀▀▀▀▄▄▄▀▀▄▄▄▄▀▀▄▄▄▄▀▀▄▄▀▄▄▀▀▀▀▄▄▄▀▀▄▄▀▄▄▀▄▄▄▀▄▄▄▀▀▀
"""
    journey_display = """
  █ █▀█ █ █ █▀█ █▄ █ █▀▀ █▄█
█▄█ █▄█ █▄█ █▀▄ █ ▀█ ██▄  █ 
"""
    map_plotting_display = """
█▀▄▀█ ▄▀█ █▀█   █▀█ █░░ █▀█ ▀█▀
█░▀░█ █▀█ █▀▀   █▀▀ █▄▄ █▄█ ░█░
"""
    wait_display = """
█▀█ █▀█ █▀█ █▀▀ █▀▀ █▀ █▀ █ █▄░█ █▀▀ ░ ░ ░   █▀█ █░░ █▀▀ ▄▀█ █▀ █▀▀   █░█░█ ▄▀█ █ ▀█▀ █
█▀▀ █▀▄ █▄█ █▄▄ ██▄ ▄█ ▄█ █ █░▀█ █▄█ ▄ ▄ ▄   █▀▀ █▄▄ ██▄ █▀█ ▄█ ██▄   ▀▄▀▄▀ █▀█ █ ░█░ ▄
"""
    map_created_display = """
█▀▄▀█ ▄▀█ █▀█   █░█ ▄▀█ █▀   █▄▄ █▀▀ █▀▀ █▄░█   █▀▀ █▀█ █▀▀ ▄▀█ ▀█▀ █▀▀ █▀▄   █▀ █░█ █▀▀ █▀▀ █▀▀ █▀ █▀ █▀▀ █░█ █░░ █░░ █▄█
█░▀░█ █▀█ █▀▀   █▀█ █▀█ ▄█   █▄█ ██▄ ██▄ █░▀█   █▄▄ █▀▄ ██▄ █▀█ ░█░ ██▄ █▄▀   ▄█ █▄█ █▄▄ █▄▄ ██▄ ▄█ ▄█ █▀░ █▄█ █▄▄ █▄▄ ░█░
"""
    choosing_vehicle_display = """
█░█ █▀▀ █░█ █ █▀▀ █░░ █▀▀   █▀▀ █░█ █▀█ █ █▀▀ █▀▀
▀▄▀ ██▄ █▀█ █ █▄▄ █▄▄ ██▄   █▄▄ █▀█ █▄█ █ █▄▄ ██▄
"""
    simulation_display = """
█▀█ █░█ █▄░█ █▄░█ █ █▄░█ █▀▀   █▀ █ █▀▄▀█ █░█ █░░ ▄▀█ ▀█▀ █ █▀█ █▄░█ ▀
█▀▄ █▄█ █░▀█ █░▀█ █ █░▀█ █▄█   ▄█ █ █░▀░█ █▄█ █▄▄ █▀█ ░█░ █ █▄█ █░▀█ ▄
"""


    def __init__(self) -> None:
        """
        This method initializes Navigation object 

        Args:
            fleet (_type_): a list of vehicles
            trip (_type_): a Trip object
        """
        # initialize a User Object
        user = User()

        # get fleet, trip, cities_list from user
        self.fleet = user.vehicles
        self.trip = user.trips
        self.cities_list = copy(self.trip.next_city)
        self.cities_list.insert(0, self.trip.departure)


        self.onboard()
    

    def display_fleet(self):
        """
        This method shows the list of vehicles that the user has chosen
        """
        # print fleet

        # count the index of the Table
        count = 0

        # print text art
        print(self.fleet_display)

        # create table
        display_table = PrettyTable(header=False, border=True)
        display_table.hrules = ALL

        # loop through the fleet
        for vehicle in self.fleet:
            # add each vehicle as a row of the table
            display_table.add_row([count + 1, vehicle])
            count += 1

        # print the table
        print(display_table)

    def display_trip(self):
        """
        This method shows the trip that the user has chosen
        """
        # print text art
        print(self.trip_display)

        # print the trip
        print(self.trip)
    
    
    def finding_path(self):
        """
        This method find the fastest vehicle, and let the user choose the vehicle (from user's fleet) for the trip
        """

        # find the fastest vehicle
        # show the path and time duration to finish the trip
        # print text art
        print(self.journey_display)


        number_of_cities = len(self.cities_list)

        # initialize fastest vehicle and the largest possible time duration
        fastest_vehicle = self.fleet[0]
        time_min = 10000000000

        # loop through the vehicles fleet
        for vehicle in self.fleet:
            
            # create a table for displaying paths
            display_table = PrettyTable(["Step", "Departure", "Destination", "Path", "Time (h)"] ,header=True, border=True)
            display_table.hrules = ALL

            # print which vehicle is used 
            display_table.title = f"Using {vehicle}, your trip will go through:"

            # calculate the total time 
            total_time = 0

            # loop through every city that the user have chosen
            for i in range(number_of_cities - 1):
                
                # find shortest path between 2 cities
                departure = self.cities_list[i]
                destination = self.cities_list[i + 1]
                path = find_shortest_path(vehicle, departure, destination)

                # time to travel between these 2 cities
                time = path.total_travel_time(vehicle)

                # add to the total time of the whole journey
                total_time += time

                # add row to the table 
                display_table.add_row([i + 1, departure, destination, path, time])

            # print the table
            print(display_table)

            # print the total time of the whole trip
            print(f"This whole journey will take approximately {int(total_time)} hours for {vehicle}\n")

            # find the fastest vehicle
            if time_min > total_time:
                time_min = total_time
                fastest_vehicle = vehicle
            
            # show the fastest vehicle
        print(f"The fastest vehicle: {fastest_vehicle}")

        # let the user choose vehicle
        print(self.choosing_vehicle_display)
        self.display_fleet()
        number_of_vehicles = len(self.fleet)
        restrict = list(range(1, number_of_vehicles + 1))

        user_input = int_input(f"Please choose your vehicle (1 -> {number_of_vehicles}): ", restricted_to=restrict)

        user_vehicle = self.fleet[user_input - 1]

        return user_vehicle


    def plotting_the_path(self, given_vehicle: Vehicle):
        """
        This method plot the trip with a given vehicle, then store the map in a file

        Args:
            given_vehicle (_type_): a Vehicle object
        """
        # print text art
        print(self.map_plotting_display)

        number_of_cities = len(self.cities_list)

        paths_list = []
        cities_list = []

        # loop through every city
        for i in range(number_of_cities - 1):

            # find the trip of the given vehicle, which will contain multiple trips
            departure = self.cities_list[i]
            destination = self.cities_list[i + 1]
            path = find_shortest_path(given_vehicle, departure, destination)
            paths_list.append(path)
        
        # create a list containing every cities from the paths_list
        cities_list.append(paths_list[0].departure)
        for path in paths_list:
            cities_list += path.next_city

        # create a Trip from cities_list 
        user_journey = Trip(cities_list[0])
        for city in cities_list[1:]:
            user_journey.add_next_city(city)
        
        # print some text art
        print(self.wait_display)

        # plot the map
        plot_trip(user_journey)

        # print some text art
        print(self.map_created_display)

        return user_journey


    def progress_bar(self, given_vehicle: Vehicle, given_journey: Trip) -> None:
        """
        This method simulates a trip

        Args:
            given_vehicle (Vehicle): 
            given_journey (Trip): 
        """
        # Print text art
        print(self.simulation_display)

        # Calculate the total time
        total_time = given_journey.total_travel_time(given_vehicle)

        # Calculate the real time that the progress bar running
        sleep_time = (0.1 * total_time) / 1000

        # Number of cities that the trip go through (from departure to destination)
        number_of_stops = len(given_journey.next_city) + 1

        arrive_time = int(1000 / (number_of_stops - 1))
        # Create the progress bar using alive-progress library
        with alive_bar(1000, title="Running Simulation", force_tty=True, monitor=False, elapsed=False, stats=False, enrich_print=False) as bar:
            j = 0
            for i in range(1, 1001):
                if i == 1:
                    print(f"You departed at {given_journey.departure}")
                elif i % arrive_time == 0 and j < number_of_stops - 1:
                    print(f"You have arrived at {given_journey.next_city[j]}")
                    j += 1
                time.sleep(sleep_time)
                bar()
        
        # print text art
        print("""
█▀ █░█ █▀▀ █▀▀ █▀▀ █▀ █▀ █▀▀ █░█ █░░   █▀ █ █▀▄▀█ █░█ █░░ ▄▀█ ▀█▀ █ █▀█ █▄░█ █
▄█ █▄█ █▄▄ █▄▄ ██▄ ▄█ ▄█ █▀░ █▄█ █▄▄   ▄█ █ █░▀░█ █▄█ █▄▄ █▀█ ░█░ █ █▄█ █░▀█ ▄
""")

    def onboard(self):
        """
        This method executes the above methods
        """
        # print some text art
        print(User.seperator)
        print(User.step_3)

        # print some information for users
        navigation_information()

        # print the fleet and trip that user has chosen
        self.display_fleet()
        self.display_trip()

        # let the user choose which vehicle
        vehicle_choice = self.finding_path()

        # plot the map to a file
        journey = self.plotting_the_path(vehicle_choice)

        # print text art
        print(User.seperator)

        # enter to continue
        enter = input(User.enter_art)

        # print text art
        print(User.seperator)

        # print Step 4
        print(User.step_4)

        # enter to continue
        enter = input("Press enter to start running simulation!")

        # display the progress bar
        self.progress_bar(vehicle_choice, journey)

        # print some text art
        print(User.seperator)


if __name__ == "__main__":
    navigate = Navigation()





