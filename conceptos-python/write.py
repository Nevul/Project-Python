#open() tiene por defecto el parámetro de lectura --> open('path', 'r')
#open('path', 'r+') --> tendrá permisos de lectura y escritura sin sobreescribir su contenido, es decir añade al contenido
#open('path', 'w+') --> tendrá permisos de escritura y lectura, pero sobreescribirá su contenido
with open('./conceptos-python/text.txt', 'w+') as file:
    for line in file:
        print(line)

    file.write('Este es un mensaje de prueba 2 para comprobar que se sobreescribe el contenido de un archivo al usar "w+"')