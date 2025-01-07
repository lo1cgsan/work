# litery.py
tekst = 'abc xyz zaq'
klucz = 3
szyfrogram = ''

for znak in tekst.upper():
    kod = ord(znak)
    if kod == 32:
        continue

    kod = kod + klucz
    if kod > 90:
        kod = kod - 26
    szyfrogram = szyfrogram + chr(kod)

print(szyfrogram)



#    if kod >= 97 and kod <= 122:
#        kod = kod - 32
