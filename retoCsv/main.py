'''
Para resolver este desafío, debes utilizar el archivo data.csv que contiene los datos de los gastos de una empresa.
El archivo tiene dos columnas: el nombre del área y el total de gastos del año.

Tu reto es implementar la función read_csv que lee el archivo CSV y calcula el total de gastos de la empresa.
Para leer el archivo CSV, puedes utilizar la función open y el módulo csv de Python. Una vez que hayas leído los datos,
puedes calcular el total de gastos implementando la lógica que consideres necesaria.
'''
import csv

def read_csv(path):
   # Tu código aquí 👇
   with open(path, 'r') as csvfile:
      reader = csv.reader(csvfile, delimiter = ',')
      values = [int(values[1]) for values in reader]
      total = sum(values)
   return total

if __name__ == '__main__':
   total = read_csv('./retoCsv/data.csv')
   print(f'Gastos totales => {total}')