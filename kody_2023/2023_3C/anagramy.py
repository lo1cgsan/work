# dane wejściowe
w1 = input("Podaj wyraz w1: ")
w2 = input("Podaj wyraz w2: ")

w1 = w1.lower().replace(" ", "")
w2 = w2.lower().replace(" ", "")

if len(w1) != len(w2):
    print("Nie anagramy")
elif sorted(w1) == sorted(w2):
    print("Anagramy")

