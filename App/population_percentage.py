import read_csv
import charts

data = read_csv.read_csv('./data.csv')
data = list(filter(lambda data_dict: data_dict['Continent'] == 'South America', data))

countries = list(map(lambda data_dict: data_dict['Country/Territory'], data))
percetanges = list(map(lambda data_dict: data_dict['World Population Percentage'], data))

charts.generate_pie_chart(countries, percetanges)