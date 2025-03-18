# liczby_abc.py
# Pobierz 3 różne liczby całkowite a, b, c i wypisz najmniejszą.

# dane wejściowe
a = int(input('Liczba a: '))
b = int(input('Liczba b: '))
c = int(input('Liczba c: '))

# szukamy najmniejszej
if a < b:
    if a < c:
        print(f'a = {a}')
    else:
        print(f'c = {c}')
else:
    if b < c:
        print(f'b = {b}')
    else:
        print(f'c = {c}')


if a < b:
    if a < c:
        print(f'a = {a}')
    else:
        print(f'c = {c}')
elif b < c:
    print(f'b = {b}')
else:
    print(f'c = {c}')
