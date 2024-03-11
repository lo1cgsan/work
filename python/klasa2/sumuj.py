liczba = int(input("Podaj liczbę: "))
suma = 0
licznik = 0

while liczba != 0:
    suma += liczba
    licznik += 1
    liczba = int(input("Podaj liczbę: "))

print(suma)
