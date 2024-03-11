import datetime

imie = input("Podaj imię: ")
# print(imie)
print("Cześć", imie, "Jestem Python!")
# print(type(imie))

wiek = input("Ile masz lat? ")
# print(type(wiek))

dzis = datetime.date.today()
rok = dzis.year
# print(type(rok))

rok_urodzenia = rok - int(wiek)
print(f"Urodziłeś się w {rok_urodzenia} roku.")
