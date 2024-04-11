def oblicz_srednia(lista, n):
    suma = 0
    for i in range(n):
        # print(i, lista[i])
        suma = suma + lista[i]
    print(suma / n)


def oblicz_srednia2(lista, n):
    suma = 0
    for element in lista:
        suma = suma + element
    print(suma / n)


ile_ocen = int(input('Ile ocen? '))
oceny = [] # utworzenie pustej listy

# for i in range(ile_ocen):
while len(oceny) < ile_ocen:
    ocena = int(input('Podaj ocenę: '))
    if ocena > 0 and ocena <= 6:
        oceny.append(ocena) # dopisz element do listy
    else:
        print("Błędna ocena!")

oblicz_srednia(oceny, ile_ocen)
oblicz_srednia2(oceny, ile_ocen)
