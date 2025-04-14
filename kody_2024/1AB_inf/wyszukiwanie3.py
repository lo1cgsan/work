# Napisz program, który sprawdza, czy podany element jest na liscie.

liczby = [5, 8, -1, 12, 0, 6, -1, 10]
n = len(liczby)

szukany = int(input('Podaj liczbę: '))

# przeszukiwanie liniowe
# maks. liczba porównań to n
indeks = -1
for i in range(n):
    if liczby[i] == szukany:
        indeks = i
        break

if indeks > -1:
    print('Znaleziono na indeksie:', indeks)
else:
    print('Nie znaleziono!')
