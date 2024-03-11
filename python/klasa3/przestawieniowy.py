tekst = input("Podaj tekst: ")
klucz = int(input("Podaj klucz: "))

if len(tekst) % klucz > 0:
    tekst = tekst + (klucz - len(tekst) % klucz) * "."

print(tekst)

# 0123 4567 891011
# ALAM
# AKOT
# A. . .

# AAALK.AO.MT.
# 0, 4, 8
# 1, 5, 9
# 2, 6, 10
# 3, 7, 11
szyfrogram = ""

for i in range(klucz):
    for j in range(len(tekst) // klucz):
        szyfrogram += tekst[i + j * klucz]

print(szyfrogram)

# 0123 4567 891011
# AAA
# LK.
# AO.
# MT.
# 0 3 6 9 11

tekst = ""
for i in range(len(szyfrogram) // klucz):
    for j in range(klucz):
        tekst += szyfrogram[i + j * klucz]

print(tekst)
