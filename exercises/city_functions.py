# 11-1 city_functions.py file for importing

def city_country(city, country):
    return f"{city.title()}, {country.title()}"


def city_country2(city, country, population):
    return f"{city.title()}, {country.title()} - population {population}"


def city_country3(city, country, population=""):
    if population:
        value = f"{city}, {country} - population {population}"
    else:
        value = f"{city}, {country}"
    return value.title()


def city_country4(city, country, population=""):
    if population:
        value = f"{city}, {country} - population {population}"
    else:
        value = f"{city}, {country}"
    return value.title()


class Employee:
    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, salary_raise=5000):
        self.annual_salary += salary_raise
