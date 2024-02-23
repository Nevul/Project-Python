import utils
import read_csv
import charts

#Al estar modularizado el código en funciones, aunque ejecutemos este archivo, no se ejecutrá nada de su código interno.



def run():
    data = read_csv.read_csv('App/data.csv')
    country = input('País: ')
    country_list_dict = utils.population_by_country(data, country)

    if len(country_list_dict) > 0:
        country_dict = country_list_dict[0]
        labels, values = utils.get_population_year(country_dict)
        charts.generate_bar_chart(labels, values)

#Con esto se puede ejecutar el código del archivo, aunque esté modularizado en funciones
    #'__main__' es independiente del nombre del archivo.
if __name__ == '__main__':
    run()