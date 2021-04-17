# Task 2
# Creating a dictionary.
# Create a function called make_country, which takes in a country’s name and capital as parameters.
# Then create a dictionary from those two, with ‘name’ as a key and ‘capital’ as a parameter.
# Make the function print out the values of the dictionary to make sure that it works as intended.
def make_country(name, capital):
    my_countries = {}
    my_countries['name'] = name
    my_countries['capital'] = capital

    for key, value in my_countries.items():
        my_countries[key] = value
    return my_countries


print(make_country('Ukraine', 'Kiev'))
