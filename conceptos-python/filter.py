numbers = [1, 2, 3, 4, 5]

#filter() no altera el archivo original, y sirve para seleccionar elementos de un iterable en base a una condición
pares = list(filter(lambda element: element % 2 == 0, numbers))
print(f'pares => {pares}')