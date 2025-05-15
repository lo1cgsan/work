# Napisz progam, który pobiera n ocen i wypisuje ich  średnią.

def srednia(oceny, n):
    suma = 0
    for i in range(n):
        print("Indeks:", i)
        suma += oceny[i]
    print(suma / n)

n = int(input('Ile ocen: '))
oceny = []  # utworzenie pustej listy

# for i in range(n):
while len(oceny) < n:
    ocena = int(input('Podaj ocenę: '))
    if ocena > 0 and ocena < 7:
        oceny.append(ocena)  # dodajemy element do listy
    else:
        print('Błędna ocena!')

print(oceny)
srednia(oceny, n)
