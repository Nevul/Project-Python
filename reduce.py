import functools

numbers = [2, 2, 5, 7, 2]

#reduce() requiere una función y un iterable, la función toma 2 argumentos que serán: acumulador e iterador. En ese orden
#Según la condición que indiquemos, el acumulador actuará de una u otra forma.
print(f'Número mayor de la lista {numbers}')
max_number = functools. reduce(lambda x, y: x if x > y else y, numbers)
print(f'Max number => {max_number}')

def select_max_number(x, y):
    print(f'x => {x}')
    print(f'y => {y}')
    return x if x > y else y

max_number_2 = functools. reduce(select_max_number, numbers)
print(max_number_2)
#----------------------------------------------------------------
print(f'Suma de números de la lista {numbers}')
sum_number = functools. reduce(lambda x, y: x + y, numbers)
print(f'Suma de => {sum_number}')

def sum_number_func(x, y):
    print(f'x => {x}')
    print(f'y => {y}')
    return x + y

sum_number = functools. reduce(sum_number_func, numbers)
print(sum_number)