tekst = 'abc xyz zaq'
szyfrogram = ''
klucz = 3

for znak in tekst.upper().replace(' ', ''):
    kod = ord(znak)
    kod = kod + klucz
    if kod > 90:
        kod = kod - 26
    szyfrogram = szyfrogram + chr(kod)

print(szyfrogram)
