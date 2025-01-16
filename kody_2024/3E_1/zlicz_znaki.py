tekst = "Jakiś ciąg znaków."

samogloski = "aoueyiąęó"

licznik = 0
inne = 0  # spacje i znaki interpunkcyjne
ile_znakow = 0  # licznik wszystkicj znaków
for znak in tekst.upper():
    ile_znakow += 1
    if znak in samogloski.upper():
        licznik += 1

    # for samogloska in samogloski.upper():
    #    if znak == samogloska:
    #        licznik = licznik + 1

    kod = ord(znak)
    if kod < 65 or kod > 90:
        inne += 1

print(tekst)
print(ile_znakow)
print(licznik)
print(ile_znakow - licznik - inne)
