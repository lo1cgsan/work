def szyfruj(tekst, klucz):
    klucz = klucz % 26
    szyfrogram = ""

    for znak in tekst:
        kod_ascii = ord(znak) + klucz
        if kod_ascii > 90:
            szyfrogram += chr(kod_ascii - 26)
        else:
            szyfrogram += chr(kod_ascii)

    return szyfrogram


def deszyfruj(szyfrogram, klucz):
    klucz = klucz % 26
    tekst = ""

    for znak in szyfrogram:
        kod_ascii = ord(znak) - klucz
        if kod_ascii < 65:
            tekst += chr(kod_ascii + 26)
        else:
            tekst += chr(kod_ascii)

    return tekst

tekst = input("Podaj tekst: ")
tekst = tekst.upper().replace(" ", "")
klucz = int(input("Podaj klucz: "))

print(szyfruj(tekst, klucz))
