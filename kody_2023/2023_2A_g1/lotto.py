from random import randint


def czy_zapisana(liczba, lista):
    for element in lista:
        if element == liczba:
            return True
    return False


wylosowane = []
# for i in range(3):
while len(wylosowane) < 3:
    liczba = randint(1, 10)
    if not czy_zapisana(liczba, wylosowane):
        wylosowane.append(liczba)

typy = []
while len(typy) < 3:
    liczba = int(input("Podaj liczbę 1-10: "))
    if not czy_zapisana(liczba, typy):
        typy.append(liczba)

trafione = 0
for typ in typy:
    if czy_zapisana(typ, wylosowane):
        trafione += 1

print(wylosowane)
print(typy)
print(trafione)
