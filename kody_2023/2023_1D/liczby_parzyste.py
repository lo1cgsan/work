"""
liczby_parzyste.py
Napisz program, który pobiera
5 liczb, zlicza i sumuje
liczby parzyste, a na koniec
wypisuje te informacje.
"""
suma = 0
licznik = 0

for i in range(5):
    a = int(input("Podaj liczbę: "))
    if a % 2 == 0:
        suma = suma + a
        licznik = licznik + 1

print(suma)
print(licznik)

