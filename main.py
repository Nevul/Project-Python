'''
from pkg.mod_1 import func_1
from pkg.mod_2 import *     #de este modo se importan todas las funciones del módulo

print(func_1())
print(func_3())
print(func_4())
'''

import pkg
print(pkg.URL)
#-------------------------------------
#import implícito de una función, utilizando namespaces
#para que funcione, se debe declarar el import desde el archivo __init__.py
print(pkg.mod_1.func_1())