from locations import City, Country, test_example_countries_and_cities
import csv

def create_cities_countries_from_CSV(path_to_csv: str) -> None:
    """
    Reads a CSV file given its path and creates instances of City and Country for each line.
    """
    # open csv file
    with open(path_to_csv, 'r', encoding="utf-8") as data:

        # read the file into multiple lines
        lines = list(csv.reader(data, delimiter=","))

        # get the header
        header = lines[0]

        # base on the header, get the index of "city_ascii", "lat", "lng", "country", "iso3", "capital", "id"
        city_name_index = header.index("city_ascii")
        lat_index = header.index("lat")
        long_index = header.index("lng")
        country_index = header.index("country")
        iso3_index = header.index("iso3")
        capital_index = header.index("capital")
        id_index = header.index("id")

        # loop through the data
        for line in lines[1:]:
                # create Country instances
            Country(line[country_index], line[iso3_index])
        
        for line in lines[1:]:
                # create City instances
            City(line[city_name_index], line[lat_index], line[long_index], line[country_index], line[capital_index], line[id_index])

if __name__ == "__main__":
    create_cities_countries_from_CSV("worldcities_truncated.csv")
    test_example_countries_and_cities()









