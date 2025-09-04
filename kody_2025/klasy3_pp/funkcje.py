def wypisz_znak(z, n):
    for _ in range(n):
        print(z)

def policz_parzyste(n, m):
    licznik = 0
    for i in range(n, m+1):
        if i % 2 == 0:
            licznik += 1
    return licznik

def oblicz_nwd(a, b):
    while a != b:
        print(a, b)
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

# wypisz_znak('%', 10)
# ile = policz_parzyste(3, 65)
# print(ile)
nwd = oblicz_nwd(1000, 2)
print(nwd)

