def get_population():
    countries = ['ecu', 'col', 'per']
    population = [18, 51, 33]
    return countries, population

def population_by_country(data, country):
    result = list(filter(lambda item: item['country'] == country, data))
    return result

name = 'Alex'
age = 28
sex = 'Male'