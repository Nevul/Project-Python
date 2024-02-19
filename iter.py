for i in range(1, 10):
    print(i)

iter = iter(range(1, 4))   #esto arroja un objeto iterable
print(iter)
print(next(iter))   #next() itera manualmente un objeto iterable, 1 a la vez
print(next(iter))   #cada vez que invoquemos next(), el objeto iterable se iterará 1 vez.
print(next(iter))   #tener en cuenta, que cuando se salga del límite del objeto iterable, dará un ERROR
print(next(iter))