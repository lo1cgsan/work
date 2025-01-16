tekst = "Jakiś tekst, który zawiera samogłoski"

samogloski = "aoueyiąęó"


licznik = 0
licznik_dodatkowe = 0
for znak in tekst.upper():
    if znak in samogloski.upper():
        licznik = licznik + 1

    kod = ord(znak)
    if kod < 65 or kod > 90:
        licznik_dodatkowe = licznik_dodatkowe + 1

print(licznik)
print(len(tekst) - licznik - licznik_dodatkowe)
