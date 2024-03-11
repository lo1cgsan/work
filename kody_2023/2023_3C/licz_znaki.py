# dane wejściowe
tekst = 'Przykładowy jakiś tekst'
samogloski = 'aoóeyiąę'
spolgloski = 'bcdfghjklmnprstuwxyz'
licznik = 0
l_spacji = 0
l_sam = 0
l_spol = 0
l_inne = 0

# obliczenia lub inne operacje
print(tekst)

for znak in tekst:
    licznik += 1
    if znak == " ":
        l_spacji += 1
    elif znak in samogloski:
        l_sam += 1
    elif znak in spolgloski:
        l_spol += 1


# dane wyjściowe
print("Znaków:", licznik)
print("Wyrazów:", l_spacji + 1)
print("Samogłoski:", l_sam)
print("Spółgłoski:", l_spol)
print("Inne:", l_inne)

