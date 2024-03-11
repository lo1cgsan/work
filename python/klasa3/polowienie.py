from random import randint

def szukaj_bin(lista, szukany):
    n = len(lista)
    poczatek = 0
    koniec = n - 1
    licznik = 0
    while poczatek <= koniec:
        srodek = (poczatek + koniec) // 2
        licznik += 1
        #print(srodek)
        if lista[srodek] == szukany:
            print("Licznik:", licznik)
            return srodek
        if szukany < lista[srodek]:
            koniec = srodek - 1
        else:
            poczatek = srodek + 1
    print("Licznik:", licznik)
    return -1

lista = [88]lo1
for i in range(10000):
    lista.append(randint(0, 1000000))
szukany = 88
print(szukaj_bin(lista, szukany))


        
        
