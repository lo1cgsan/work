# Napisz program, który pobiera podaną przez użytkownika liczbę ocen
# i wypisuje ich średnią oraz najmniejszą i największą z nich.

def pobierz_oceny(n):
    for i in range(n):
        ocena = int(input("Podaj ocenę: "))
        oceny.append(ocena)


def oblicz_srednia(oceny, n):
    suma = 0
    for i in range(n):
        suma = suma + oceny[i]
    return suma / n


oceny = []
n = int(input("Ile ocen? "))
pobierz_oceny(n)
print(oceny)
print(oblicz_srednia(oceny, n))
