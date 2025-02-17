indeksy= 0, 1, 2, 3, 4, 5
lista = sorted([4, 8, 1, 2, 5, 0])
print(lista)
szukany = 4

for el in lista:
    if el == szukany:
        print('znalazłem')
        exit()

print('nie znalazłem')

def szukaj_bin(lista, el):
    lewy, prawy = 0, len(lista) - 1
    while lewy <= prawy:
        srodek = (lewy + prawy) // 2
        print(srodek)
        if lista[srodek] == el:
            return srodek
        if lista[srodek] < el:
            lewy = srodek + 1
        else:
            prawy = srodek - 1
    return -1

print(szukaj_bin(lista, szukany))
