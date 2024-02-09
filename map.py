# Map nos permite transformar una lista o iterable a través de una función.
# entregándonos otra lista o iterable del mismo número de elementos.
numbers_1 = [1, 2, 3, 4]
result_1 = list(map(lambda x: x * 2, numbers_1))
print(result_1)

numbers_2 = [4, 3, 5, 6, 1]
numbers_3 = [3, 7, 2, 1]

print("*" * 20)
print(f"numbers_2 => {numbers_2}")
print(f"numbers_2 => {numbers_3}")

result_2 = list(map(lambda n2, n3: n2 * n3, numbers_2, numbers_3))
print(f"result_2 => {result_2}")

print("*" * 20)
numbers_4 = []

for element in numbers_1:
    numbers_4.append(element + 2)

print(f"numbers_4 => {numbers_4}")