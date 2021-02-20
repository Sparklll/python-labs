import logging
import sys
from signal import signal, SIGINT
from countryinfo import CountryInfo

logger = logging.getLogger('')
logger.setLevel(logging.INFO)

console_handler = logging.StreamHandler(sys.stdout)
console_formatter = logging.Formatter("%(message)s")
console_handler.setFormatter(console_formatter)
console_handler.setLevel(logging.INFO)

logger.addHandler(console_handler)

def print_country_info():
    country_name = input('Please, enter country name to retrieve info: ')
    try:
        country_info = CountryInfo(country_name)
        country_capital = country_info.capital()
        country_region = country_info.region()
        country_area = country_info.area()
        country_population = country_info.population()
        country_residents = country_info.demonym()

        info_str = (
        "Name : {name} \n".format(name=country_name) +
        "Capital : {capital} \n".format(capital=country_capital) +
        "Region : {region} \n".format(region=country_region) +
        "Area : {area} sq.km \n".format(area=country_area) +
        "Population : {population} people \n".format(population=country_population) +
        "Residents : {residents} \n".format(residents=country_residents))

        logger.info(info_str)

    except ValueError:
        logger.info("Sorry, country not founded :(")

def handler(signal_received, frame):
    logger.info('\nSIGINT or CTRL-C detected. Exiting gracefully')
    exit(0)

def main():
    signal(SIGINT, handler)
    print_country_info()

if __name__ == '__main__':
    main()
