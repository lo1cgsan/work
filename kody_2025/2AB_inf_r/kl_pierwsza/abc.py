"""
ZADANIE
Pobierz trzy liczby całkowite, sprawdź,
która jest najmniejsza, i wypisz ją.
"""
a = int(input('Podaj a: '))
b = int(input('Podaj b: '))
c = int(input('Podaj c: '))

if a < b and a < c:
    print(a)
elif b < a and b < c:
    print(b)
if c < a and c < b:
    print(c)
