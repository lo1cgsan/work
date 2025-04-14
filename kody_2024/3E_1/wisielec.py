from random import randint
slowa = [
    'Warszawa', 'Londyn',
    'Paryż', 'Sztokholm',
    'Sofia',
    'Ateny',
    'Rzym',
    'Madryt',
]
n = len(slowa)
indeks = randint(0, n-1)
slowo = slowa[indeks]
print(slowo)
