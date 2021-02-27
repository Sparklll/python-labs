#!/usr/bin/env python

import logging
import sys

from countryinfo import CountryInfo

logging.basicConfig(level=logging.INFO, stream=sys.stdout, format="%(message)s")
logger = logging.getLogger(__name__)


def main():
    country_name = input("Please, enter country name to retrieve info: ")
    try:
        country_info = CountryInfo(country_name)
        country_capital = country_info.capital()
        country_region = country_info.region()
        country_area = country_info.area()
        country_population = country_info.population()
        country_residents = country_info.demonym()
    except KeyError:
        logger.info("Sorry, country not founded :(")
    else:
        total_info = (
            f"Name: {country_name}\n"
            f"Capital : {country_capital}\n"
            f"Region : {country_region}\n"
            f"Area : {country_area} sq.km\n"
            f"Population : {country_population} people\n"
            f"Residents : {country_residents}"
        )
        logger.info(total_info)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logger.info("\nSIGINT or CTRL-C detected. Exiting gracefully")
        sys.exit(130)
