# petla_for.py

n = int(input('Ile ocen? '))

suma = 0
licznik = 0
for i in range(n):
    ocena = int(input('Podaj ocenę: '))
    if ocena > 0 and ocena < 7:
        suma = suma + ocena
        licznik = licznik + 1
    else:
        print('Błędne dane!')

print('Liczba ocen:', licznik)
print('Średnia ocen:', suma/licznik)
