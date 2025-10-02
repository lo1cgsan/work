# dane wejściowe
cenak = float(input('Podaj cenę komputera: '))
cenap = float(input('Podaj cenę płyty: '))
w = int(input('Podaj % wzrostu ceny płyty głównej: '))

# operacje
# (10%, 20%>
if w > 10:
    if w <= 20:
        cenap = cenap * (1 + w / 100)
        cenak = cenak + 0.05 * cenap
        print('Nowa cena komputera:', cenak)
    else:
        print('Za wysoka cena!')
else:
    print('Cena komputera bez zmian:', cenak)
