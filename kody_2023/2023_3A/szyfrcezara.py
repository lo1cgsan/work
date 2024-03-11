def szyfruj(teskt, klucz):
    szyfrogram = ""
    for znak in tekst:
        kod_ascii = ord(znak)
        kod_ascii = kod_ascii + klucz
        if kod_ascii > 122:
            kod_ascii = kod_ascii - 26
        szyfrogram = szyfrogram + chr(kod_ascii)
    return szyfrogram


def deszyfruj(szyfrogram, klucz):
    tekst = ""
    for znak in szyfrogram:
        kod_ascii = ord(znak)
        kod_ascii = kod_ascii - klucz
        if kod_ascii < 97:
            kod_ascii = kod_ascii + 26
        tekst = tekst + chr(kod_ascii)
    return tekst

# dane wejściowe
tekst = input("Podaj tekst: ")
klucz = int(input("Podaj klucz: "))

tekst = tekst.lower().replace(" ", "")
klucz = klucz % 26

szyfrogram = szyfruj(tekst, klucz)
print(szyfrogram)
tekst = deszyfruj(szyfrogram, klucz)
print(tekst)
