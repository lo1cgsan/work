from random import randint

n = int(input('Ile liczb? '))
start = 1
stop = 10

liczby = []  # utworzenie pustej listy
while len(liczby) < n:
    liczba = randint(start, stop)
    czy liczba jest w liście:
    liczby.append(liczba)

typy = []  # utworzenie pustej listy
for i in range(n):
    liczba = int(input('Podaj typ: '))
    typy.append(liczba)

trafione = []  # utworzenie pustej listy
for i in range(n):
    for j in range(n):
        if liczby[i] == typy[j]:
            trafione.append(liczby[i])

print(liczby)
print(typy)
print(trafione)
