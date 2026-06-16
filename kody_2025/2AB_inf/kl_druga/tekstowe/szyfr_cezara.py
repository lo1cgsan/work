def szyfruj(tekst, klucz):
    # algorytm
    szyfrogram = ''
    #for i in range(len(tekst)):
    #    znak = tekst[i]

    for znak in tekst:
        kod = ord(znak) + klucz
        if kod > 90:
            kod -= 26
        szyfrogram += chr(kod)
    return szyfrogram

def deszyfruj(szyfrogram, klucz):
    tekst = ''
    for znak in szyfrogram:
        kod = ord(znak) - klucz
        if kod < 65:
            kod += 26
        tekst += chr(kod)
    return tekst

# dane wejściowe
tekst = 'aBc, XyZ.'
klucz = 55 % 26

for znak in ' ,.':
    tekst = tekst.replace(znak, '')
tekst = tekst.upper()
print(tekst)

#dane wyjściowe
szyfrogram = szyfruj(tekst, klucz)
print('Szyfrogram:', szyfrogram)

# deszyfracja
tekst = deszyfruj(szyfrogram, klucz)
print('Tekst:', tekst)
