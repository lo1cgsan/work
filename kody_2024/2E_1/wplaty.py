kwota = float(input('Podaj kwotę: '))

suma_wplat = 0

# for i in range(3):
while suma_wplat < kwota:
    wplata = float(input('Podaj wpłatę: '))
    suma_wplat += wplata

print('Wpłacono:', suma_wplat)
