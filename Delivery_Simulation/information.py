from prettytable import PrettyTable, ALL
from get_input import int_input

from locations import Country

def background_information(name):
    """
    This function provides the information and guidelines

    Args:
        name (_type_): _description_
    """
    print(f"""
-------------------------------------------------------------------------
Hi {name}! 

░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗  ░█████╗░███╗░░██╗  ██████╗░░█████╗░░█████╗░██████╗░██████╗░
░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝  ██╔══██╗████╗░██║  ██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗
░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░  ██║░░██║██╔██╗██║  ██████╦╝██║░░██║███████║██████╔╝██║░░██║
░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░  ██║░░██║██║╚████║  ██╔══██╗██║░░██║██╔══██║██╔══██╗██║░░██║
░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗  ╚█████╔╝██║░╚███║  ██████╦╝╚█████╔╝██║░░██║██║░░██║██████╔╝
░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝  ░╚════╝░╚═╝░░╚══╝  ╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░

Pierre's side business, Papa Pierre's Pâtisseries, delivers French yumminess to almost a thousand major locations around the world thanks to its technologically-advanced fleet of vehicles

In this program, you will be able to: 
    - Travel by choosing from our numerous example fleet of vehicles, and example of trips
    - Create your own fleet with custom parameters
    - Create your own trip by manually adding all cities
    - Find the shortest path between two given cities for 1 vehicle or a fleet of vehicle
    - Find the fastest vehicle that can do your trip
From that, we will plot your trip on a file that you can saved.


██╗░░░░░███████╗████████╗  ████████╗██╗░░██╗███████╗  ░░░░░██╗░█████╗░██╗░░░██╗██████╗░███╗░░██╗███████╗██╗░░░██╗  ██████╗░███████╗░██████╗░██╗███╗░░██╗██╗
██║░░░░░██╔════╝╚══██╔══╝  ╚══██╔══╝██║░░██║██╔════╝  ░░░░░██║██╔══██╗██║░░░██║██╔══██╗████╗░██║██╔════╝╚██╗░██╔╝  ██╔══██╗██╔════╝██╔════╝░██║████╗░██║██║
██║░░░░░█████╗░░░░░██║░░░  ░░░██║░░░███████║█████╗░░  ░░░░░██║██║░░██║██║░░░██║██████╔╝██╔██╗██║█████╗░░░╚████╔╝░  ██████╦╝█████╗░░██║░░██╗░██║██╔██╗██║██║
██║░░░░░██╔══╝░░░░░██║░░░  ░░░██║░░░██╔══██║██╔══╝░░  ██╗░░██║██║░░██║██║░░░██║██╔══██╗██║╚████║██╔══╝░░░░╚██╔╝░░  ██╔══██╗██╔══╝░░██║░░╚██╗██║██║╚████║╚═╝
███████╗███████╗░░░██║░░░  ░░░██║░░░██║░░██║███████╗  ╚█████╔╝╚█████╔╝╚██████╔╝██║░░██║██║░╚███║███████╗░░░██║░░░  ██████╦╝███████╗╚██████╔╝██║██║░╚███║██╗
╚══════╝╚══════╝░░░╚═╝░░░  ░░░╚═╝░░░╚═╝░░╚═╝╚══════╝  ░╚════╝░░╚════╝░░╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚══════╝░░░╚═╝░░░  ╚═════╝░╚══════╝░╚═════╝░╚═╝╚═╝░░╚══╝╚═╝
-------------------------------------------------------------------------""")

def custom_vehicles_information():
    """
    This function provides the information about custom vehicles
    """
    print("""
-------------------------------------------------------------------------
Our business have 3 different types of vehicles: 

    1. Crappy Crepe Car: 
        - A flying car that can travel between any two cities in the world, but moves pretty slowly.
        - You can custom the speed of this vehicle.

    2. Diplomacy Donut Dinghy: 
        - A small boat which is licensed to travel on diplomatic hyperlanes. So it moves extra fast between capital cities. 
        - It can also travel between any two cities in the same country. 
        - However, it can only move from one country to another via their capitals.
        - You can custom the speed within a country, and the speed between different countries.
    
    3. Teleporting Tarte Trolley:
        - A trolley bus that can teleport between any two cities if they are close enough, regardless of countries. 
        - Because teleportation technology is still in its infancy, it takes time to program and execute a blink between two cities.
        - You can custom the execution time, and the distance the vehicle travel in 1 time of teleportation.
-------------------------------------------------------------------------""")


def example_vehicles_information():
    """
    This function provides the information about example vehicles
    """
    print("""
-------------------------------------------------------------------------
Our business have 3 different types of vehicles: 

    1. Crappy Crepe Car: 
        - A flying car that can travel between any two cities in the world, but moves pretty slowly.

    2. Diplomacy Donut Dinghy: 
        - A small boat which is licensed to travel on diplomatic hyperlanes. So it moves extra fast between capital cities. 
        - It can also travel between any two cities in the same country. 
        - However, it can only move from one country to another via their capitals.
    
    3. Teleporting Tarte Trolley:
        - A trolley bus that can teleport between any two cities if they are close enough, regardless of countries. 
        - Because teleportation technology is still in its infancy, it takes time to program and execute a blink between two cities.
-------------------------------------------------------------------------""")


def example_trip_information():
    """
    this function provides the information about example trips
    """
    # create a table
    display_table = PrettyTable(["Index","Continent", "Country", "City 1", "City 2"], border=True)
    display_table.hrules = ALL
    # add rows to the table
    display_table.add_row([1, "Australia", "Australia" , "Melbourne", "Sydney"])
    display_table.add_row([2, "Asia", "Vietnam" ,"Hanoi", "Ho Chi Minh City"])
    display_table.add_row([3, "Europe", "France", "Paris", "Marseille"])
    display_table.add_row([4, "North America", "USA", "New York", "Richmond"])
    display_table.add_row([5, "South America", "Brazil", "Sao Paulo", "Rio de Janeiro"])
    display_table.add_row([6, "Africa", "Nigeria", "Lagos", "Kano"])

    print(f"""
-------------------------------------------------------------------------
Our business offer multiple trips across 6 countries. 
Each country belongs to 1 continent, and will have 2 cities!
You can create a trip by choosing 1 departure and 1 destination

{display_table}

-------------------------------------------------------------------------""")

def custom_trip_information():
    """
    This function provides information about customizing user own trip
    """
    print("""
-------------------------------------------------------------------------
    Our business provides trips all over the world!
    You can create your own custom trip by manually adding each cities as a stop within your trip
        (1) Select how many stop that you want to have in your trip
        (2) Select the country -> our program will show all the cities that belong to that country and available in our data base
        (3) Select the city from the table, remember that you cannot choose 2 identical cities twice in a row
        (4) Repeat step (2) and (3) until you have enough of stops in your trip
        (5) If you change your mind, you can re-do everything start from step (1)

    Good luck with your trip!
-------------------------------------------------------------------------""")


def countries_name():
    """
    This function ask the user if he/she want to see list of countries
    """
    print("Next, you will have to choose the country of the city that you want to add into the trip!")

    # get the input
    user_choice = int_input("Do you want to see the names of every countries? (0 for NO / 1 for YES): ", restricted_to=[0, 1])

    # if the user want to see the contries list
    if user_choice == 1:
        # create a table to display countries
        country_table = PrettyTable(border=True, header=False)
        country_list = []

        # loop through the list of countries
        for country in Country.countries.keys():
            
            # add to country_list
            country_list.append(country)

            # if there are 8 countries in country_list, we add the country_list to the table
            if len(country_list) == 8:
                # each row of the table will have 8 countries
                country_table.add_row(country_list)

                # reset the country_list to empty for the next loop
                country_list = []

        # print the table
        print(country_table)
    else:
        print("Okay! You are smart!\n")


def navigation_information():
    """
    This function provides information for navigating onboard, after the users have chosen their fleet of vehicles, and their trip
    """
    print("""
-------------------------------------------------------------------------
    Our business provides features to navigate your trip while on board:
        - Find the fastest vehicle as well as the shortest path of the trip that you have chosen
        - After finding the path, we can plot a trip on a map that is saved to a file.
-------------------------------------------------------------------------""")