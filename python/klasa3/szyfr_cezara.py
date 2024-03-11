# szyfr_cezara.py

def szyfruj(tekst, klucz):
    szyfrogram = ''
    for znak in tekst.upper():
        kod_ascii = ord(znak)
        if kod_ascii < 65 or kod_ascii > 90:
            continue
        if kod_ascii + klucz > 90:
            szyfrogram += chr(kod_ascii + klucz - 26)
        else:
            szyfrogram += chr(kod_ascii + klucz)

    return szyfrogram

def deszyfruj(szyfrogram, klucz):
    tekst_jawny = ''
    for znak in szyfrogram:
        kod_ascii = ord(znak)
        if kod_ascii - klucz < 65:
            tekst_jawny += chr(kod_ascii - klucz + 26)
        else:
            tekst_jawny += chr(kod_ascii - klucz)

    return tekst_jawny

def main():
    tekst_jawny = input("Podaj tekst: ")
    klucz = int(input("Podaj klucz: "))
    klucz = klucz % 26
    szyfrogram = szyfruj(tekst_jawny, klucz)
    print(szyfrogram)
    print(deszyfruj(szyfrogram, klucz))


main()
