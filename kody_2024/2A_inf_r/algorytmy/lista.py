from collections import deque

lista = deque()

lista.append(5)
lista.append(6)
lista.appendleft(1)
print(lista)

pozycja = 5
lista.remove(pozycja)

print(lista)

if lista:
    print('nie pusta')
else:
    print('pusta')
