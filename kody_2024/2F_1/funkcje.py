def wypisz_znak(z, n):
    for _ in range(n):
        print(z, end='')
    print()

def policz_parzyste(n, m):
    licznik = 0
    for i in range(n, m+1):
        if i % 2 == 0:
            licznik += 1
    return licznik

def oblicz_nwd():
    while a != b:
        pass

ile = policz_parzyste(3, 45)
print(ile)

# wypisz_znak('$', 1)
# wypisz_znak('@', 2)
# wypisz_znak('^', 3)
# wypisz_znak('*', 4)
