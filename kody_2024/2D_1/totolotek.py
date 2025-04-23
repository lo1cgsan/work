from random import randint

def losuj_liczby(n, a, b):
    # wylosuj n liczb i zapamiętaj je w liście liczby
    liczby = []

    licznik = 0
    while licznik < n:
        liczba = randint(a, b)
        if not liczba in liczby:
            liczby.append(liczba)
            licznik += 1

    return liczby

def pobierz_typy(n):
    # pobierz n liczb i zapamiętaj je w liście typy
    typy = []
    for i in range(n):
        typ = int(input('Podaj typ: '))
        typy.append(typ)
    return typy

def sprawdz(n, typy, liczby):
    # sprawdź, ile liczb odgadnął użytkownik
    trafione = []
    for i in range(n):
        typ = typy[i]
        for j in range(n):
            if typ == liczby[j]:
                trafione.append(typ)
    return trafione

n = int(input('Ile liczb wylosować: '))
start = 1
stop = 10

liczby = losuj_liczby(n, start, stop)
typy = pobierz_typy(n)
trafione = sprawdz(n, typy, liczby)

print(liczby)
print(trafione)
