tekst = "aBc Xyz zaq"
klucz = 123
szyfrogram = ""
print(tekst)

klucz = klucz % 26
print(klucz)

for znak in tekst.upper().replace(" ", ""):
    kod = ord(znak)
    # if 97 <= kod <= 122:
    #    kod = kod - 32
    kod = kod + klucz
    if kod > 90:
        kod = kod - 26
    szyfrogram = szyfrogram + chr(kod)
    print(znak, kod, chr(kod))

print(szyfrogram)
