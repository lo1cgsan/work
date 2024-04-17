"""
Napisz program, który wypisuje i zlicza liczby dwucyfrowe,
w których cyfry są różne. Na końcu programu wypisz
liczbę tych liczb.
"""
licznik = 0
for i in range(100):
    if i > 9 and i % 11 > 0:
        print(i)
        licznik = licznik + 1

print("Dwucyfrowych:", licznik)

