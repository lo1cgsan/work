rok = int(input("Podaj rok urodzenia: "))

if rok >= 2024:
    print("Błędny rok")
else:
    wiek = 2024 - rok

    if wiek >= 18:
        print("Pełnoletni")
    else:
        print("Niepełnoletni")

