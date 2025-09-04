# petla_for.py

n = int(input('Ile ocen: '))

suma = 0
licznik = 0
for i in range(n):
    ocena = int(input(f'Podaj ocenę {i+1}: '))
    if ocena > 0 and ocena < 7:
        licznik += 1
        suma += ocena
    else:
        print('Błędne dane!')

print('Liczba ocen:', licznik)
