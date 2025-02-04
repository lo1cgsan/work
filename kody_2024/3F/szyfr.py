tekst = 'abc xyz zaq'
szyfrogram = ''
klucz = 3

for znak in tekst.upper():
    kod = ord(znak)
    if kod == 32:
        continue
    kod = kod + klucz
#    if 97 <= kod <= 122:
#        kod = kod - 32
    if kod > 90:
        kod = kod - 26
    szyfrogram = szyfrogram + chr(kod)

print(szyfrogram)
