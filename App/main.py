import utils

countries, population = utils.get_population()
print(countries, population)
print(utils.name)
print(utils.age)
print(utils.sex)

data = [
    {
        'country': 'Ecuador',
        'population': 18000000
    },
    {
        'country': 'Perú',
        'population': 33000000
    },
    {
        'country': 'Colombia',
        'population': 51000000
    }
]

country = input('Escriba un país: ')
print(utils.population_by_country(data, country))