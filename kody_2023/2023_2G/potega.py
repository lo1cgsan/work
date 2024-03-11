# dane wejściowe
a = int(input("Podaj a: "))
n = int(input("Podaj n: "))


def potega(a, n):
wynik = 1
for i in range(n):
    wynik = wynik * a

print(wynik)
