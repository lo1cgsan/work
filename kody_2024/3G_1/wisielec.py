from random import randint

slowa = [
    'Warszawa', 'Berlin', 'Praga',
    'Paryż', 'Madryt', 'Sofia',
    'Kopenhaga', 'Sarajewo'
]

n = len(slowa)
slowo = slowa[randint(0, n-1)]

dl_slowa = len(slowo)
l1 = randint(0, dl_slowa-1)  # pozycja pierwszej litery
l2 = randint(0, dl_slowa-1)  # pozycja drugiej litery

while l1 == l2:
    l2 = randint(0, dl_slowa-1)  # pozycja drugiej litery

for i in range(dl_slowa):
    if i == l1 or i == l2:
        print(slowo[i], end='')
    else:
        print(' _ ', end='')

exit()


zycia = len(slowo)
odgadniete = 0
zgadniete_litery = []

while zycia > 0:
    odgadywane = str(input("Podaj literę lub całe słowo do sprawdzenia: "))
    if len(odgadywane) == 1:
        if odgadywane in slowo:
            if odgadywane not in zgadniete_litery:
                print("Słowo zawiera literę: ", odgadywane)
                odgadniete += slowo.count(odgadywane)
                zgadniete_litery.append(odgadywane)
            if odgadniete == len(slowo):
                break
        else:
            print("Słowo nie zawiera litery: ", odgadywane)
            zycia -= 1
    else:
        if odgadywane == slowo:
            print("Podano poprawne słowo!")
            odgadniete = len(slowo)
            break
        else:
            print("Podane słowo nie jest hasłem!")
            zycia -= 1
    print("Pozostałe życia: ", zycia)

if odgadniete == len(slowo):
    print("Udało ci się odgadnąć słowo: ", slowo)
else:
    print("Niestety nie udało ci się odgadnąć słowa: ", slowo)
