tekst = 'abcxyz'
klucz = 123
szyfrogram = ''

klucz = klucz % 26
print(klucz)

for znak in tekst.upper():
    kod = ord(znak)
    # if kod >= 97 and kod <= 122:
    #    kod = kod - 32
    kod = kod + klucz
    if kod > 90:
        kod = kod - 26
    print(znak, kod, chr(kod))
    szyfrogram = szyfrogram + chr(kod)

print(szyfrogram)
