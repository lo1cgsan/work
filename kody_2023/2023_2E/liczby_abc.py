# Napisz program, który pobiera trzy liczby całkowite
# i wypisuje najmniejszą z nich.

a = int(input("Podaj a: "))
b = int(input("Podaj b: "))
c = int(input("Podaj c: "))

# 1 2 3
# 2 1 3
# 2 3 1
# 3 2 1

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
