# dane wejściowe
w1 = input("Podaj wyraz w1: ")
w1 = w1.lower().replace(" ", "")

w2 = ""

for i in range(len(w1)-1, -1, -1):
    w2 = w2 + w1[i]

if w1 == w2:
    print("Palindrom")
else:
    print("Nie palindrom")
