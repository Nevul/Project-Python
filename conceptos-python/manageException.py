#De esta forma ejecutamos nuestro código e indicamos el tipo de error a capturar en caso de suceder.
#Si se da el error, el programa no se detiene y el tipo de error se almacena en una variable que nos indica por mensaje el error.
#Tambén podemos agrupar el código y capturar distintos tipos de errores
'''
try:
    print(0 / 0)
except ZeroDivisionError as error:
    print(error)

try:
    assert 1 != 1, 'Uno no es distinto de uno'  #Podemos poner un mensaje al AssertionError
except AssertionError as error:
    print(error)

try:
    age = 15
    if age < 18:
        raise Exception('No se permiten menores de edad')
except Exception as error:
    print(error)
'''
#Una vez que captura un error, el resto del código en (try:) se salta y ejecuta el código externo sin detener el programa.
#De esta forma agrupamos los posibles errores que se pueden dar y controlar como se manejan.
try:
    print(0 / 0)
    assert 1 != 1, 'Uno no es distinto de uno'  #Podemos poner un mensaje al AssertionError
    age = 15
    if age < 18:
        raise Exception('No se permiten menores de edad')
    
except ZeroDivisionError as error:
    print(error)
    
except AssertionError as error:
    print(error)
    
except Exception as error:
    print(error)

print('Fin')