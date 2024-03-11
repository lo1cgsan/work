"""
Napisz program, który wypisuje małe litery alfabetu łacińskiego
rosnąco, a duże litery malejąco.

Wskazówka: wykorzystaj kody ASCII.
"""
for i in range(97, 123):
    print(chr(i))

for i in range(90, 64, -1):
    print(chr(i))

"""
Zsumuj liczby parzyste w zakresie <0; 100>.
"""
suma = 0
for i in range(101):
    if i % 2 == 0:
        suma = suma + i
print(i)
