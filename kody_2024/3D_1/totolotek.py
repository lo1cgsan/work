from random import randint

liczby = []  # utworzenie pustej listy

n = 5
start = 0
stop = 20

for i in range(n):
    liczba = randint(start, stop)
    liczby.append(liczba)

print(liczby)

typy = []
for i in range(n):
    liczba = int(input('Podaj liczbę: '))
    typy.append(liczba)
