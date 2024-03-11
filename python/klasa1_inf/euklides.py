a = int(input("Podaj a: "))
b = int(input("Podaj b: "))

licznik = 0
while a != b:
    licznik = licznik + 1
    if a > b:
        a = a - b
    else:
        b = b - a

print("Licznik:", licznik, "Wynik:", a)

