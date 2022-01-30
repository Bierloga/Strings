# Do not modify these lines
__winc_id__ = 'd0d3cdcefbb54bc980f443c04ab3a9eb'
__human_name__ = 'operators'

# Add your code after this line

#The language spoken the most in Switzerland is the same as in Spain.
most_spoken_language_spain = 'Spanish'
most_spoken_language_switzerland = 'German'
print(most_spoken_language_spain == most_spoken_language_switzerland)

#The most prevalent religion in Switzerland is the same as in Spain.
most_prevalent_religion_spain = 'Roman Catholic'
most_prevalent_religion_switzerland = 'Roman Catholic'
print(most_prevalent_religion_spain == most_prevalent_religion_switzerland)

#The name length of Spain's capital does not equal that of Switzerland.
capital_spain = 'Madrid'
capital_switzerland = 'Bern'
print(len(capital_spain)!=len(capital_switzerland))

#Switzerland's GDP is greater than Spain's GDP.
gdp_spain = 1715000000000
gdp_switzerland = 590700000000
print(gdp_switzerland > gdp_spain)

#The population growth is less than 1% in Switzerland and Spain.
growth_rate_percentage_spain = -0.03
growth_rate_percentage_switzerland = 0.65
print(growth_rate_percentage_spain <1 and growth_rate_percentage_switzerland <1)

#At least one of the two countries has a population count of over 10 million.
population_spain = 47300000
population_switzerland = 8500000
print(population_spain > 10000000 or population_switzerland > 10000000)

#Exactly one of the two countries has a population count of over 10 million.
print(population_spain > 10000000 and population_switzerland <10000000)