from random import randint

n = int(input('Ile liczb? '))
start = 1
stop = 10

liczby = []
while ???
    liczba = randint(start, stop)
    for i in range(len(liczby)):
        if liczba == liczby[i]:
            pass
    liczby.append(liczba)

typy = []
for i in range(n):
    liczba = int(input('Podaj typ? '))
    typy.append(liczba)

liczby = [3, 6, 1]
typy = [5, 9, 2]

trafione = []
for i in range(n):
    for j in range(n):
        if liczby[i] == typy[j]:
            trafione.append(liczby[i])

print(liczby)
print(typy)
print(trafione)
