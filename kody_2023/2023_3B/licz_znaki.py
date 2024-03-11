# dane wejściowe
tekst = 'Przykładowy jakiś tekst'
samogloski = 'aąoóueęyi'
spolgloski = "bcdfghjklmnprstwxz"

# operacje i obliczenia
print(tekst)

licznik = 0
l_spacji = 0
l_sam = 0
l_spolg = 0
l_inne = 0

for znak in tekst: 
    licznik += 1
    if znak == " ":
        l_spacji += 1
    elif znak in samogloski:
        l_sam += 1
    elif znak in spolgloski:
        l_spolg += 1
    else:
        l_inne += 1

# dane wyjściowe
print("Znaków:", licznik)
print("Wyrazów:", l_spacji + 1)
print("Samogłosek:", l_sam)
print("Spółgłosek:", l_spolg)
print("Inne:", l_inne)

