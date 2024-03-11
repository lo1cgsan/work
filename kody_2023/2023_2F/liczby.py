a = float(input("Podaj bok: "))
b = float(input("Podaj bok: "))

pole = a * b
obwod = 2 * (a + b)

print(round(pole, 2))
print(round(obwod, 2))

if a > b:
    print(f"a({a}) > b({b})")
elif a < b:
    print(f"a({a}) < b({b})")
else:
    print(f"a({a}) == b({b})")


for i in range(5):
    print(i)
    


