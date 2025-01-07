from math import sqrt

n = 100
lista = [True] * n
lista[0] = False
for i in range(2, round(sqrt(n)) + 1):
    if lista[i]:
        for j in range(i+i, n, i):
            lista[j] = False

for i in range(1, n):
    if lista[i]:
        print(i, end=' ')
