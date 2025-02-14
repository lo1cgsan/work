from collections import deque

def przejdz(krok, pozycja):
    return pozycja + krok


lista = deque()
n = 10
krok = 2

for i in range(n):
    lista.append(i + 1)

print(*lista)

pozycja = przejdz(krok, 1)
while len(lista) > 1:
    lista.remove(pozycja)
    print(*lista)
    pozycja = przejdz(krok, pozycja)
