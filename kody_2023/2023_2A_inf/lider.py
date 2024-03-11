from random import randint

def generuj_zbior(n):
    zbior = []
    for i in range(2*n):
        zbior.append(randint(1, 3))
    return(zbior)


def policz_elementy(zbior):
    maks_el = 0 # maksymalna liczba wystąpień
    najczestsza = 0 # najczęściej występujący element
    for liczba in zbior:
        badany = 0
        for liczba2 in zbior:
            if liczba == liczba2:
                badany += 1
        if maks_el < badany:
            maks_el = badany
            najczestsza = liczba

    if (maks_el > len(zbior)/2):
        print("Lider:", najczestsza)
    else:
        print("Brak lidera!")


def znajdz_lidera(zbior):
    n = len(zbior)
    licznik = 0
    for i in range(n):
        if not licznik:
            lider = zbior[i]
            licznik = 1
        elif lider == zbior[i]:
            licznik += 1
        else:
            licznik -= 1
        print(lider, licznik)
    return licznik, lider


def sprawdz_lidera(zbior, licznik, lider):
    if not licznik:
        print("Brak lidera")
    else:
        licznik = 0 
        for l in zbior:
            if lider == l:
                licznik += 1
    if licznik > len(zbior)/2:
        print(f"Lider: {lider}, {licznik}")
    else:
        print("Brak lidera!")

n = 10
# zbior = generuj_zbior(n)
zbior = [1, 1, 1, 3, 1, 5, 5, 1]
# policz_elementy(zbior)
print(zbior)
licznik, lider = znajdz_lidera(zbior)
sprawdz_lidera(zbior, licznik, lider)


