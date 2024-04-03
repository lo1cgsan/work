"""
Napisz program, który wylosuje 3 niepowtarzające się liczby
z zakresu <1; 10>.
"""

from random import randint

x = randint(1, 10)
y = randint(1, 10)

for i in range(10):
    if y == x:
        y = randint(1, 10)
    else:
        break # przerwij pętlę

z = randint(1, 10)


for i in range(10):
    if z == x or z == y:
        z = randint(1, 10)
    else:
        break # przerwij pętlę

print(x, y, z)
