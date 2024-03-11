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
klucz = len(tekst) // 2 - 1

for i in range(0, len(tekst), klucz):
    for j in range(klucz):
        print(tekst[i+j], end='')
    print()
