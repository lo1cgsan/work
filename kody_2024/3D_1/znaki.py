"""
Kody ASCII i szyfr Cezara
"""
tekst = input('Podaj tekst: ')
klucz = int(input('Podaj klucz: '))
klucz = klucz % 26
szyfr = ''

for znak in tekst.upper():

    kod = ord(znak)  # odczytanie kodu ASCII

    if kod == 32:
        continue

    if kod + klucz > 90:
        szyfr += chr(kod + klucz - 26)
    else:
        szyfr += chr(kod + klucz)

print(szyfr)
