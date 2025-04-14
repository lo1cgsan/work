from random import randint

slowa = [
    'Warszawa', 'Praga', 'Berlin', 'Sofia',
    'Wiedeń', 'Londyn', 'Paryż', 'Monako',
    'Sarajewo'
]

n = len(slowa)
indeks = randint(0, n-1)
slowo = slowa[indeks]
print(slowo)
