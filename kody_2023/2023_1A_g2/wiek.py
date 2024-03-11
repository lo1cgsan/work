# Napisz program, który pobiera rok urodzenia,
# oblicza wiek użytkownika i wypisuje komunikat
# "Pełnoletni" lub "Niepełnoletni".

# dane wejśiowe
rok_urodzenia = int(input("Podaj rok urodzenia: "))

# obliczenia
wiek = 2024 - rok_urodzenia

# dane wyjściowe
if wiek >= 18:
    print("Pełnoletni")
else:
    print("Niepełnoletni")

