# Napisz program, który pobiera trzy liczby całkowite
# i wypisuje najmniejszą z nich.

#a = int(input("Podaj a: "))
#b = int(input("Podaj b: "))
#c = int(input("Podaj c: "))

# Ile program wykonuje porównań?
a, b, c = 1, 2, 3  # 2 porównania
a, b, c = 2, 1, 3
a, b, c = 3, 2, 1
a, b, c = 2, 3, 1  # 2 porównań

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
