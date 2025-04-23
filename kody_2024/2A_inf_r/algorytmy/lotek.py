import random

n = int(input("Ile typów? "))
zakres = int(input("Podaj zakres: "))
liczby = []  # lista liczb

# wylosuj n unikalnych liczb
i = n
while i > 0:
    liczba = random.randint(0, zakres)
    if liczba not in liczby:
        liczby.append(liczba)
        i = i - 1

# pobierz n unikalnych typów od użytkownika
typy = []
i = n
while i > 0:
    liczba = int(input('Podaj typ: '))
    if liczba not in typy and liczba > 0 and liczba <= zakres:
        typy.append(liczba)
        i = i - 1
    else:
        print('Błędne dane!')

# sprawdzanie za pomocą pętli
trafione = 0
for x in typy:
    if x in liczby:
        trafione += 1

trafione = set(liczby) & set(typy)

print('Trafione:', trafione)
print(len(trafione))
