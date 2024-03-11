# dane wejściowe
w1 = input("Podaj wyraz 1 ")
w2 = input("Podaj wyraz 2 ")

w1 = w1.lower()
w2 = w2.lower()
w1 = w1.replace(" ", "")
w2 = w2.replace(" ", "")

if len(w1) != len(w2):
    print("Nie anagramy")
elif sorted(w1) == sorted(w2):
    print("Anagramy")
