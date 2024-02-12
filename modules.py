import sys
print(sys.path)

import re
text = 'Estoy a 3 meses de cumplir 29 años. Para ese tiempo estaré trabajando o a su vez trabajando y en la Maestría en Automatización y Control, la cual me va a costar unos $2900. Es probable que mi trabajo dure unos 6 meses a un capital libre de unos $500 que sumado al capital de renta de la vivienda, durante la maestría, debería ser de unos $200 mensual. Es decir, unos $5400 hasta finalizar la maestría de 1 año, que restando unos $500 por percances, sería un total de $4900.'
extract_numbers = re.findall('[0-9]+', text)
print(extract_numbers)

import time
timestamp = time.time()
print(timestamp)

local = time.localtime()
print(local)

ascii_local = time.asctime(local)
print(ascii_local)

import collections
numbers = [2,1,4,1,31,31,2,4,2,6,4,3,3,6,3]
counter = collections.Counter(numbers)
print(counter)