country_list = ["Holland", "Belgium", "Germany", "Russia", "France"]

def test_function():
    parent_list = []
    for country in country_list:
        child_list = []
        country = country.lower()
        for element in country:
            if element == 'a' or element == 'o' or element == 'i' or element == 'e' or element == 'u':
                child_list.append(element)
        parent_list.append(child_list)
    print(parent_list)


test_function()
