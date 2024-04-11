"""
Napisz program, który wypisze i zliczy wszystkie dwucyfrowe liczby,
ale tylko takie, w których cyfry są różne.
Na końcu wypisz liczbę takich liczb.
"""
licznik = 0
for i in range(100):
    if i > 9 and i % 11 != 0:
        print(i)

print(licznik)
