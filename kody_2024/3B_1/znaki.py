# operacje znakach
tekst = 'abc xyz stw'
klucz = 38
szyfrogram = ''

klucz = klucz % 26
for znak in tekst:
    kod = ord(znak)
    if kod == 32:
        continue
    if kod >= 97 and kod <= 122:
        kod = kod - 32
    kod = kod + klucz
    if kod > 90:
        kod = kod - 26
    szyfrogram = szyfrogram + chr(kod)
    print(znak, kod, chr(kod))

print(tekst, szyfrogram)
