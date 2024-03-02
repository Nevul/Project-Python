file = open('conceptos-python/text.txt') #esto abre el archivo y ocupa espacio de memoria hasta que se cierre con name.close()

#print(file.read())     #lee todo el documento
print(file.readline())  #readline() sin parámetros leerá toda la línea
print(file.readline(4)) #readline(4) continuará con la lectura desde el punto anterior hasta 4 caracteres
print(file.readline())  #readline() continuará la lectura desde el punto anterior hasta completar la línea
print('-------------------------')
#file es un iterable, donde cada elemento es una línea de texto
for line in file:       #esto continúa la lectura desde el punto leído previamente
    print(line)

file.close()

print('-------------------------')
#Esta es otra forma de abrir un archivo para su manipulación o lectura. A diferencia del método anterior,
#aquí no debemos preocuparnos por cerrar el archivo con name.close(), el archivo se cierra automáticamente
#una vez que termina su código interno.
with open('conceptos-python/text.txt') as file:
    for line in file:
        print(line)