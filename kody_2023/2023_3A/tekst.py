# dane wejściowe
tekst = "Jakiś tekst przykładowy"
samogloski = "aąeęioóuy"
spolgloski = "bcdfghjklłmnprstwvxz"


# operacje i obliczenia
print(tekst)
print(len(tekst))

licz_spacji = 0
licz_sam = 0
licz_spol = 0
licz_inny = 0

for znak in tekst:
    if znak == " ":
        licz_spacji += 1
    elif znak in samogloski:
        licz_sam += 1
    elif znak in spolgloski:
        licz_spol += 1
    else:
        licz_inny += 1


# dane wyjściowe
print("Wyrazów", licz_spacji + 1)
print("Samogłosek", licz_sam)
print("Spółgłoski", licz_spol)
print("Inne", licz_inny)
    
