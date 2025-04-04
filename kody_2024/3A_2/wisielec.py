from random import randint

slowa = [
    'Praga', 'Berlin', 'Warszawa',
    'Londyn', 'Sofia', 'Paryż',
    'Wiedeń', 'Sztokholm', 'Sarajewo',
    'xxx'
]
n = len(slowa)
k = randint(0, n-1)
print(slowa[k])

dl_slowa = len(slowa[k])
i = randint(0, dl_slowa-1)
j = randint(0, dl_slowa-1)
for l in range(dl_slowa):
    if l == i or l == j:
        print(slowa[k][l], end='')
    else:
        print(' _ ', end='')
