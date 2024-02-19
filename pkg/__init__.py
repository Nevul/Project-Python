#Para versiones anteriores a Python v3.3, es obligatorio la creación de este archivo con el nombre exacto.
#Caso contrario no se podrá importar paquetes.
#También suele crearse este archivo y dejarse vacío, ya que es solo por cuestiones de compatibilidad.
# - Cuando se importe un paquete se iniciará este archivo y todo su contenido, sin embargo solo será una vez.
# - Es decir, aunque se llame 2+ veces al paquete, solo se iniciará una vez el archivo __init__.py

print('Se inición el paquete')
URL = 'lxnevul.com'

import pkg.mod_1, pkg.mod_2