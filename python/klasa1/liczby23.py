# Napisz program, który wypisuje liczby dwucyfrowe
# w których cyfry nie powtarzają się.
# Nie wypisujemy: 11, 22, 33, ...

licznik = 0
for ld in range(1, 10):
    for lj in range(0, 10):
        if ld != lj:
            print("Ld:", ld, "Lj:", lj)
            licznik += 1  # inkrementacja o 1
    print()

print("Licznik:", licznik)
