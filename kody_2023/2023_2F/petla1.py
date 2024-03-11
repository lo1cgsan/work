ile_liczb = int(input("Ile ocen? "))
suma = 0

for liczba in range(ile_liczb):
    ocena = int(input("Podaj ocenę? "))
    suma = suma + ocena
    print(suma, ocena)
    
print(suma/ile_liczb)
