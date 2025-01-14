# zlicz_znaki.py

tekst = "Lorem Ipsum is simply dummy text of"

licznik = 0

samogloski = ['a', 'o', 'u', 'e', 'y', 'i']

for znak in tekst.upper():
    if znak in samogloski:
        licznik = licznik + 1

    # kod = ord(znak)
    # if kod == 65 or kod == 69 or kod == 79:
    #     licznik = licznik + 1

print(licznik)
