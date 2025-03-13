from sys import getsizeof

# typy proste
znak = 'ą'
l_int = 100000000
l_float = 12000000.5
warunek = False

print(znak, getsizeof(znak))
print(l_int, getsizeof(l_int))
print(l_float, getsizeof(l_float))
print(warunek, getsizeof(warunek))

# typ złożony
tekst = 'abc'
print(tekst, getsizeof(tekst))

lista = list(range(10))
lista = [1, 1, 1, 0, 45, 'a', 'abc']
print(lista, getsizeof(lista))

slownik = {1: 'I', 2: 'II', 5: 'V', 7: 'VII'}
print(slownik, getsizeof(slownik))

zbior = {1, 'I', 1, 'II', 2, 1, 1}
print(zbior, getsizeof(zbior))

# indeksowanie
print(tekst[0], tekst[len(tekst) - 1])
print(lista[0], lista[len(lista) - 1])

# klucze
print(slownik[5], slownik[1])

# zawieranie
print(1 in zbior, 'ab' in zbior)
