def pobierz_oceny(n, oceny):
    for i in range(n):
        ocena = int(input("Podaj ocenę (1-6): "))
        while ocena < 1 or ocena > 6:
            print("Błędna ocena!")
            ocena = int(input("Podaj ocenę (1-6): "))
        oceny.append(ocena)
            

def policz_srednia(oceny):
    n = len(oceny)
    suma = 0
    for i in range(n):
        suma = suma + oceny[i]
    return suma / n

oceny = []  # pusta lista
n = int(input("Ile ocen? "))
pobierz_oceny(n, oceny)
print(oceny)

print(policz_srednia(oceny))
