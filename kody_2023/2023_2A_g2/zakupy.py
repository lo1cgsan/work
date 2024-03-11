# Napisz program, który pobiera podane przez użytkownika
# kwoty wydane na podaną przez użytkownika liczbę zakupów,
# a następnie oblicza i wypisuje średnią cenę zakupów.

l_zakupow = int(input("Ile rachunków? "))

suma = 0

for i in range(l_ocen):
    kwota = float(input("Podaj kwotę: "))
    suma = suma + kwota
    
print(suma / l_zakupow)

