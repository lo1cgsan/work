from random import randint

# n = 100
# liczby = []
# for i in range(n):
#    liczby.append(randint(1, n))
#    liczby.sort()


def szukaj_liniowo(szukany):
    for i in range(n):
        if liczby[i] == szukany:
            return i
    return 0


liczby = range(10)
n = len(liczby)


def szukaj_binarnie(lewy, prawy, szukany):
    srodek = (lewy + prawy) // 2
    if lewy > prawy:
        return -1
    if liczby[srodek] == szukany:
        print("Znaleziony")
        return srodek
    if liczby[srodek] < szukany:
        szukaj_binarnie(srodek + 1, prawy, szukany)
    else:
        szukaj_binarnie(lewy, srodek - 1, szukany)


def binarne(lewy, prawy, szukany):
    while lewy <= prawy:
        srodek = (lewy + prawy) // 2
        if liczby[srodek] == szukany:
            return srodek
        else:
            if liczby[srodek] < szukany:
                lewy = srodek + 1
            else:
                prawy = srodek - 1
    return -1


# print(szukaj_liniowo(5))
# print(szukaj_liniowo(163))

print(szukaj_binarnie(0, n - 1, 5))
# print(szukaj_binarnie(0, n - 1, 10))
