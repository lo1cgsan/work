for i in range(128):
    print(f'Kod = {i}\tZnak = {chr(i)}')


tekst = 'Imię i nazwisko'
for z in tekst:
    print(f'Znak: {z}\tKod = {ord(z)}')

# Wypisz alfabet łaciński w odwróconej kolejności
# za pomocą dużych liter
for i in range(90, 64, -1):
    print(chr(i))

# Wypisz tekst pobrany z klawiatury z odwróconą wielkością liter.
# AbCDe => aBcdE
