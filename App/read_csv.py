import csv
def read_csv(path):
    with open(path) as csvfile:
        reader = csv.reader(csvfile, delimiter = ',')   #delimiter es el separador de los campos en el archivo csv
        header = next(reader)   #leemos la 1ra fila que contiene los nombres de las columnas
        data = []
        for row in reader:
            iterable = zip(header, row)     #combina los nombres de las columnas con los valores de las filas
            data_dict = {key: value for key, value in iterable} #dict comprehension que extrae los pares key: value del iterable
            data.append(data_dict)  #añade cada diccionario a la lista vacía
        return data #retorna una lista de diccionarios

#Permite la ejecución del archivo como script desde una consola
if __name__ == '__main__':
    data = read_csv('./data.csv')
    print(data)