"""

klucz = 3

012   345   678
ALA\n MAK\n OTA

ALA
MAK
OTA

AMOLATAKA

TO BE OR NOT TO BE
klucz = 5

TOBEO/nRNOTT/nTOBE.

TOTEORT.BNO.EOB.
"""
tekst = input("Podaj tekst: ")
tekst = tekst.upper().replace(" ", "")
dl_tekstu = len(tekst)
klucz = dl_tekstu // 2 - 1
ile_wierszy, reszta = divmod(dl_tekstu, klucz)

if ile_wierszy * klucz < dl_tekstu:
    ile_wierszy += 1
    ile_dodac = ile_wierszy * klucz - dl_tekstu
    tekst += ile_dodac * '_'
    print(dl_tekstu, klucz, ile_wierszy, reszta, ile_dodac, tekst)

for i in range(0, len(tekst), klucz):
    for j in range(klucz):
        print(tekst[i+j], end='')
    print()

for i in range(klucz):
    for j in range(ile_wierszy):
        print(tekst[klucz * j + i], end='')
print()