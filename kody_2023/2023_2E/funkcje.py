# potęgowanie

def potega(a, n):
    wynik = 1

    for i in range(n):
        wynik = wynik * a

    return wynik


a = int(input("Podaj a: "))
n = int(input("Podaj n: "))

print(potega(a, n))

p1 = potega(a, n)
print(p1 + p1)
