tekst = "abcxyz"
klucz = 3

print(tekst)

for znak in tekst:
    kod = ord(znak)
    if 97 <= kod <= 122:
        kod = kod - 32
    kod = kod + klucz
    if kod > 90:
        kod = kod - 26
    print(znak, kod, chr(kod))
