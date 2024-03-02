import copy
items = [
    {
        'product': 'camisa',
        'price': 80
    },
    {
        'product': 'pantalón',
        'price': 110
    },
    {
        'product': 'corbata',
        'price': 30
    }
]

prices = list(map(lambda item: item['price'], items))
print(f'prices => {prices}')

def add_taxes(item):
    #Otra forma de solucionar la alteración por referencia de memoria
    #new_item = item.copy()
    item['tax'] = item['price'] * .15   #Exactamente en esta línea es donde se cambia los datos por referencia de memoria
    return item['tax']

print('Antes:')
print(items)

# copy.deepcopy() crea un objeto completamente nuevo.
# Si se llama directamente a la lista en ves de crear una copia de ella, la lista original se altera, ya que no se crea un objeto..
# ..nuevo y solo se aumenta la cantidad de referencias al objeto creado originalmente, es decir cualquier cambio afecta al objeto original.
#Por ello crear un nuevo objeto, servirá para que a pesar de ser modificado no altere la información dle objeto original.
taxes = list(map(add_taxes, copy.deepcopy(items)))  #copy.deepcopy(list_to_copy) permite que no se altere la lista original

print('Después:')
print(items)

print(f'taxes => {taxes}')