def oblicz_srednia(lista, n):
    suma = 0
    for i in range(n):
        print(i)
        suma = suma + lista[i]

    srednia = suma / n
    print(srednia)


oceny = []
l_ocen = int(input('Podaj liczbę ocen: '))

for i in range(l_ocen):
    ocena = int(input('Podaj ocenę: '))

    while ocena < 1 or ocena > 6:
        ocena = int(input('Podaj ocenę: '))

    oceny.append(ocena)

print(oceny)
oblicz_srednia(oceny, l_ocen)





