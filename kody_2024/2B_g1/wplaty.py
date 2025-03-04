kwota = float(input('Podaj kwotę: '))
suma_wplat = 0

while suma_wplat < kwota:
    wplata = float(input('Podaj wpłatę: '))
    suma_wplat += wplata
    print(f'Suma bieżąca: {suma_wplat}')

print(f'Suma wpłat: {suma_wplat}')
print(f'Nadpłata: {suma_wplat - kwota}')

