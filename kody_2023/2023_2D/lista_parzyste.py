"""
Napisz program, który pobierze 10 liczb od użytkownika
i zapisze je w liście. Następnie policzy i zsumuje liczby
parzyste, które znalazły się w liście.
"""
liczby = []

for i in range(10):
    liczba = int(input('Podaj liczbę: '))
    liczby.append(liczba)

print(liczby)

for i in range(10):
    if liczby[i] % 2 == 0:
        licznik = licznik + 1 # zwiększenie licznika o 1
        suma = suma + liczby[i]

print(licznik, suma)
