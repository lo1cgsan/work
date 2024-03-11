znak = input("Podaj znak: ")
licznik = 0
licznik_liter = 0

while znak != ".":
    licznik += 1
    if 65 <= ord(znak.upper()) <= 90:
        licznik_liter += 1
    znak = input("Podaj znak: ")

print(licznik)
print(licznik_liter)
