# Napisz program, który pobiera podaną przez użytkownika liczbę ocen
# semestralnych, a następnie oblicza i wypisuje ich średnią.
n = int(input("Ile ocen? "))
suma = 0

for i in range(n):
    ocena = int(input("Podaj ocenę: "))
    suma = suma + ocena

print(suma / n)
    
