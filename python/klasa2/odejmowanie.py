odjemna = int(input("Podaj odjemną: "))
odjemnik = int(input("Podaj odjemnik: "))
licznik = 0

while odjemna - odjemnik > 0:
    licznik = licznik + 1
    odjemna = int(input("Podaj odjemną: "))
    odjemnik = int(input("Podaj odjemnik: "))    

print("Liczba dodatnich wyników:", licznik)
