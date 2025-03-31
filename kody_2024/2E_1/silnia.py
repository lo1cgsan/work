# silnia.py

def silnia_iter(n):
    wynik = 1

    if n > 1:
        for i in range(2, n + 1):
            print(wynik, i)
            wynik = wynik * i
    return wynik

def silnia_rek(n):
    if n == 0:
        return 1
    else:
        wynik = n * silnia_rek(n - 1)
        print(wynik)
        return wynik

rezultat = silnia_iter(5)
print(rezultat)
print(20 * '@#')
rezultat = silnia_rek(5)
print(rezultat)
