# dane wejściowe
rok_urodzenia = int(input("Podaj rok urodzenia: "))

aktualny_rok = 2024

if rok_urodzenia >= aktualny_rok:
    print("Błędne dane")
else:
    # obliczenia
    wiek = aktualny_rok - rok_urodzenia

    # dane wyjściowe
    if wiek >= 18:
        print("Pełnoletni")
    else:
        print("Niepełnoletni")

