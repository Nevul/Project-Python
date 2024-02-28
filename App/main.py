import utils
import read_csv
import pandas as pd
import charts

#Al estar modularizado el código en funciones, aunque ejecutemos este archivo, no se ejecutrá nada de su código interno.
def run():
    '''
    #-----------------option 1-----------------
    data = read_csv.read_csv('./data.csv')
    continent = input('Continente: ')

    data = list(filter(lambda data_dict: data_dict['Continent'] == continent, data))
    countries = list(map(lambda data_dict: data_dict['Country/Territory'], data))
    percetanges = list(map(lambda data_dict: data_dict['World Population Percentage'], data))
    charts.generate_pie_chart(continent, countries, percetanges)
    #------------------End option 1-----------------
    '''
    #------------------option 2-----------------
    df = pd.read_csv('./data.csv')
    continent = input('Continente: ')
    df = df[df['Continent'] == continent]

    countries = df['Country/Territory'].values
    percetanges = df['World Population Percentage'].values
    
    charts.generate_pie_chart(continent, countries, percetanges)
    data = read_csv.read_csv('./data.csv')
    #------------------End option 2-----------------

    country = input('País: ')
    country_list_dict = utils.population_by_country(data, country)

    if len(country_list_dict) > 0:
        country_dict = country_list_dict[0]
        labels, values = utils.get_population_year(country_dict)
        charts.generate_bar_chart(country_dict['Country/Territory'], labels, values)

#Con esto se puede ejecutar el código del archivo, aunque esté modularizado en funciones
    #'__main__' es independiente del nombre del archivo.
if __name__ == '__main__':
    run()