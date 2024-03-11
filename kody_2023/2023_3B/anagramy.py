# dane wejściowe
wyraz1 = input("Podaj wyraz 1: ")
wyraz2 = input("Podaj wyraz 2: ")

wyraz1 = wyraz1.lower().replace(" ", "")
wyraz2 = wyraz2.lower().replace(" ", "")

if len(wyraz1) != len(wyraz2):
    print("Nie anagramy")
elif sorted(wyraz1) == sorted(wyraz2):
    print("Anagramy")
else:
    print("Nie anagramy")
