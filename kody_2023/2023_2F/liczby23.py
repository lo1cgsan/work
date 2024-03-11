# Napisz program, który wypisuje liczby dwucyfrowe, w których
# cyfra jedności jest różna od cyfry dziesiątek.
# Nie wypisuj: 11, 22, 33, 44 itd.
# Na koniec program powinien wypisać liczbę dwucyfrowych liczb
# o różnych cyfrach.


# zagnieżdżone instrukcje iteracyjne
licznik = 0
for ld in range(1, 10):  # pętla zewnętrzna
    for lj in range(0, 10):  # pętla wewnętrzna
        if ld != lj:
            print("Ld:", ld, "Lj:", lj)
            licznik = licznik + 1
    print()

print("Licznik:", licznik)
