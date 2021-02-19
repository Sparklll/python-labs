from countryinfo import CountryInfo


def print_country_info():
    country_name = input('Please, enter country name to retrieve info: ')
    try:
        country_info = CountryInfo(country_name)
        country_capital = country_info.capital()
        country_region = country_info.region()
        country_area = country_info.area()
        country_population = country_info.population()
        country_residents = country_info.demonym()

        print("""\
        Name : {name}
        Capital : {capital}
        Region : {region}
        Area : {area} sq.km
        Population : {population} people
        Residents : {residents}
        """.format(name=country_name,
                   capital=country_capital,
                   region=country_region,
                   area=country_area,
                   population=country_population,
                   residents=country_residents))

    except:
        print("Sorry, country not founded :(")


if __name__ == '__main__':
    print_country_info()
