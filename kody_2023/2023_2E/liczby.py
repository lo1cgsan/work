a = float(input("Podaj bok: "))
b = float(input("Podaj bok: "))
pole = a * b
obwod = 2 * (a + b)
print(pole, obwod)
print(round(pole, 2), round(obwod, 2))

if a > b:
    print("a > b")
elif a < b:
    print("a < b")
else:
    print("a == b")

for i in range(1, 11):
    if i % 2 == 1:
        print(i)



