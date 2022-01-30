from helpers import get_countries


""" Leave this untouched. Wincpy uses it to match this assignment with the
tests it runs. """
__winc_id__ = "c545bc87620d4ced81cbddb8a90b4a51"
__human_name__ = "for"


""" Write your functions here. """


def shortest_names(countries):
    shortest_length = 999
    short_country_list = []
    for country in countries:
        if len(country) < shortest_length:
            shortest_length = len(country)
    for country in countries:
        if (len(country) == shortest_length):
            short_country_list.append(country)
    print(short_country_list)


def most_vowels(countries):
    country_list_vowels = []
    for country in countries:
        country = country.lower()
        per_country_vowel_list = []
        for element in country:
            if (element == 'a' or element == 'o' or element == 'i' or element == 'e' or element == 'u'):
                per_country_vowel_list.append(element)
        country_list_vowels.append(len(per_country_vowel_list))
    highest_number_of_vowels = []
    max_value = max(country_list_vowels)
    max_index = country_list_vowels.index(max_value)
    highest_number_of_vowels.append(countries[max_index])
    country_list_vowels.remove(country_list_vowels[max_index])
    max_value = max(country_list_vowels)
    max_index = country_list_vowels.index(max_value)
    highest_number_of_vowels.append(countries[max_index])
    country_list_vowels.remove(country_list_vowels[max_index])
    max_value = max(country_list_vowels)
    max_index = country_list_vowels.index(max_value)
    highest_number_of_vowels.append(countries[max_index+2])
    country_list_vowels.remove(country_list_vowels[max_index])
    print(highest_number_of_vowels)


# This block is only run if this file is the entrypoint; python main.py
# It is not run if it is imported as a module: `from main import *`
if __name__ == "__main__":
    countries = get_countries()
    shortest_names(countries)
    most_vowels(countries)
