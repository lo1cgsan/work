# silnia.py

def silnia_iter(n):
    wynik = 1
    if n > 1:
        for i in range(2, n + 1):
            print(wynik)
            wynik = wynik * i
    return wynik

def silnia_rek(n):
    if n == 0:
        return 1
    else:
        wynik = n * silnia_rek(n - 1)
        print(wynik)
        return wynik

print(silnia_iter(10))
print(silnia_rek(10))
