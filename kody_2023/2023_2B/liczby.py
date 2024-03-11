# dane wejściowe
a = float(input("Podaj bok: "))
b = float(input("Podaj bok: "))

# obliczenia
pole = a * b
obwod = 2 * (a + b)

# dane wyjściowe
print(round(pole, 2))
print(round(obwod, 2))

if a > b:
    print("a > b")
elif a < b:
    print("a < b")
else:
    print("a == b")

for i in range(5):
    print(i)

