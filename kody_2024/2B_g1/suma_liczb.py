# suma_liczb.py
# Napisz program, który pobiera liczby z klawiatury
# aż ich suma przekroczy 75.
# Wypisz sumę oraz liczbę podanych liczb.

suma = 0
licznik = 0

while suma <= 75:
    liczba = int(input('Podaj liczbę: '))
    suma += liczba
    licznik += 1

print(f'Suma: {suma}')
print(f'Licznik: {licznik}')

