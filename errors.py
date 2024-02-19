#Cada vez que da error, el programa se detiene

#SyntaxError
#print(0 / 0))

#ZeroDivisionError
#print(0 / 0)

#NameError
#print(name)

#AssertionError
'''
print('Alex inicio')
suma = lambda a, b: a * b
assert suma(3, 4) == 10 #assert sirve para verificar una expresión lógica, si es falso, da error y si es correcto,
                        #no pasa nada y continúa el programa.
print('Alex fin')
'''

#Aquí generamos nosotros mismos una Exception o Error.
age = 8

if age < 18:
    raise Exception('No se permiten menores de edad')