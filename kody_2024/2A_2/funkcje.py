def wypisz_znak(z, n):
    for _ in range(n):
        print(z, end='')
    print()

def policz_parzyste(n, m):
    jaja = 0
    for i in range(n, m+1):
        if i % 2 == 0:
            jaja += 1
    return jaja

def oblicz_nwd(a, b):
    while a != b:
        print(a, b)
        if a > b:
            a = a -b
        else:
            b = b - a
    return a

nwd = oblicz_nwd(2, 1000000000)
print(nwd)

# wypisz_znak('$', 1)
# ile = policz_parzyste(3, 45)
# print(ile)
# wypisz_znak('o', ile)
