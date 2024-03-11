# Zadanie:
# Napisz program, który pobiera trzy liczby całkowite
# i wypisuje najmniejszą z nich.

# 1 2 3
# 2 1 3
# 2 3 1

a = int(input("Podaj liczbę a: "))
b = int(input("Podaj liczbę b: "))
c = int(input("Podaj liczbę c: "))

if a < b:
    if a < c:
        print(a)
    else:
        print(c)
else:
    if b < c:
        print(b)
    else:
        print(c)
