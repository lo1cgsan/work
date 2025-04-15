from random import randint
slowa = [
    'Warszawa', 'Berlin', 'Praga',
    'Paryż', 'Madryt', 'Rzym',
    'Sofia', 'Lisbona', 'Wiedeń'
]
n = len(slowa)
indeks = randint(0, n-1)
slowo = slowa[indeks]

print(slowo)

dl_slowa = len(slowo)
indeks1 = randint(0, dl_slowa-1)
indeks2 = randint(0, dl_slowa-1)

for i in range(dl_slowa):
    if i == indeks1 or i == indeks2:
        print(slowo[i], end='')
    else:
        print(' _ ', end='')
