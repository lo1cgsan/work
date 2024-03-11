def szyfruj(tekst, klucz):
    szyfrogram = ''

    for znak in tekst:
        kod_ascii = ord(znak) + klucz

        if kod_ascii > 90:
            kod_ascii = kod_ascii - 26

        szyfrogram = szyfrogram + chr(kod_ascii)

    return szyfrogram


def deszyfruj(szyfrogram, klucz):
    tekst = ''

    for znak in szyfrogram:
        kod_ascii = ord(znak) - klucz

        if kod_ascii < 65:
            kod_ascii = kod_ascii + 26

        tekst = tekst + chr(kod_ascii)

    return tekst


tekst = input("Podaj tekst: ").upper().replace(' ', '')
klucz = 3

szyfrogram = szyfruj(tekst, klucz)
print(szyfrogram)
tekst = deszyfruj(szyfrogram, klucz)
print(tekst)
