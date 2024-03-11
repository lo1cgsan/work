def oblicz_srednia(oceny, ile):
    suma = 0
    for i in range(ile):
        suma = suma + oceny[i]

    srednia = suma / ile
    print(srednia)


ile = int(input("Ile ocen? "))
oceny = [] # utworzenie pustej listy
liczba_poprawnych = 0

for i in range(ile):
    ocena = int(input("Podaj ocenę: "))

    if ocena > 0 and ocena < 7:
        oceny.append(ocena)
        liczba_poprawnych += 1

print(oceny)
oblicz_srednia(oceny, liczba_poprawnych)

"""
Napisz program, który pobiera tyle ocen, ile poda użytkownik oraz oblicza i wypisuje ich średnią.
"""
