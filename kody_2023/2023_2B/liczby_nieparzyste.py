"""
Napisz program, który zlicza i wypisuje liczby nieparzyste
w zakresie <n, m> podanym przez użytkownika. Na końcu program
powinien wypisać liczbę wypisanych liczb.
"""

n = int(input('Podaj n: '))
m = int(input('Podaj m: '))
licznik = 0

for i in range(n, m+1):
    if i % 2 == 1:
        print(i)
        licznik = licznik + 1

print(licznik)
