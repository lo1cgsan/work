"""
Napisz program, który wypisuje i zlicza wszystkie liczby dwucyfrowe
w zakresie <1; 100>, w których cyfry się nie powtarzają.
Na końcu wypisz liczbę takich liczb.
"""
licznik = 0
for i in range(1, 10):
    for j in range(1, 10):
        if i != j:
            licznik = licznik + 1
            print(i, j, sep='')

print("Liczba:", licznik)
