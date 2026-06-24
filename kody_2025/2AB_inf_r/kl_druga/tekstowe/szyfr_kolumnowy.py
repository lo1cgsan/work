def szyfruj(tekst, klucz):
    szyfrogram = ''
    for i in range(klucz):
        for j in range(i, len(tekst), klucz):
            szyfrogram += tekst[j]
    return szyfrogram

# dane wejściowe
tekst = 'ALA MA KOTY TRZY'
tekst = tekst.replace(' ', '')
# 0 1 2 3 4 5 6 7 8
# A L A M A K O T Y
klucz = 4
# AMOLATAKY
# A L A
# M A K
# O T Y

# 0 1 2
# 3 4 5
# 6 7 8

# 0 3 6 1 4 7 2 5 8
n = len(tekst)

if n % klucz > 0:
    tekst += (klucz - (n % klucz)) * '_'

for i in range(len(tekst)):
    print(tekst[i], end=' ')
    if (i+1) % klucz == 0:
        print()

szyfrogram = szyfruj(tekst, klucz)
print(szyfrogram)
tekst = deszyfruj(szyfrogram)
print(tekst)
