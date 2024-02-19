import utils

#Al estar modularizado el código en funciones, aunque ejecutemos este archivo, no se ejecutrá nada de su código interno.

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

def run():   
    countries, population = utils.get_population()
    print(countries, population)
    print(utils.name)
    print(utils.age)
    print(utils.sex)

    country = input('Escriba un país: ')
    print(utils.population_by_country(data, country))

#Con esto se puede ejecutar el código del archivo, aunque esté modularizado en funciones
    #'__main__' es independiente del nombre del archivo.
if __name__ == '__main__':
    run()