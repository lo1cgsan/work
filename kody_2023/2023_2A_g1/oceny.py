# Napisz program, który pobiera podaną przez użytkownika
# liczbę ocen semestralnych, a następnie oblicza i wypisuje
# ich średnią.

l_ocen = int(input("Ile ocen? "))

suma = 0

for i in range(l_ocen):
    ocena = int(input("Podaj ocenę: "))
    suma = suma + ocena
    
print(suma / l_ocen)

