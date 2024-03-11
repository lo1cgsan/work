def oblicz_srednia(oceny, ile):
    # print(oceny)
    suma = 0
    for i in range(ile):
        # print(oceny[i])
        suma += oceny[i]
    srednia = suma / ile

    return srednia


def oblicz_srednia2(oceny):
    return sum(oceny) / len(oceny)


def oblicz_srednia3(oceny):
    suma = 0
    licznik = 0
    for ocena in oceny:
        suma += ocena
        licznik += 1

    srednia = suma / licznik
    return srednia


def znajdz_min_max(oceny):
    ile = len(oceny)

    for i in range(ile-1):
        print(i)
        if oceny[i] < oceny[i+1]:
            min_w = oceny[i]

    print("Wartość min:", min_w)


znajdz_min_max([1, 4, 2, 3, 2])

ile = int(input('Ile ocen? '))
oceny = [] # pusta lista

for i in range(ile):
    a = 0
    # if a in [1, 2, 3, 4, 5, 6]:
    # if a > 0 and a < 7:
    while a < 1 or a > 6:
        a = int(input('Podaj ocenę: '))
    oceny.append(a)


srednia = oblicz_srednia(oceny, ile)
print(srednia)

srednia = oblicz_srednia2(oceny)
print(srednia)
