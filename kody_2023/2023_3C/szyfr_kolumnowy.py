"""
ALAMAKOTA
klucz = dlugosc / 2 - 1 = 3

ALA
MAK
OTA

AMO LAT AKA

TOBEO
RNOTT
OBE..

TRO ONB BOE ET. OT.
"""
tekst = input("Podaj tekst: ")
tekst = tekst.upper().replace(" ", "")
klucz = len(tekst) // 2 - 1

licznik = 0
for znak in tekst:
    print(znak, end='')
    licznik = licznik + 1
    if licznik == klucz:
        print()
        licznik = 0

print()
for i in range(klucz):
    for j in range(i, len(tekst), klucz):
        print(tekst[j], end='')

