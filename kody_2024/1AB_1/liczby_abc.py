a = int(input('Podaj liczbę a: '))
b = int(input('Podaj liczbę b: '))
c = int(input('Podaj liczbę c: '))

najmniejsza = None

if a < b:
    if a < c:
        najmniejsza = a
elif b < c:
    najmniejsza = b
else:
    najmniejsza = c

if a < b:
    if a < c:
        najmniejsza = a
    else:
        najmniejsza = c
else:
    if b < c:
        najmniejsza = b
    else:
        najmniejsza = c

print(najmniejsza)
