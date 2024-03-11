# liczby.py

a = float(input("Podaj bok: "))
b = float(input("Podaj bok: "))

pole = a * b
obwod = 2 * (a + b)

print(f"Pole: {pole}\nObwód: {obwod}")

if a > b:
    print(f"a({a}) > b({b})")
elif a < b:
    print(f"a({a}) < b({b})")
else:
    print(f"a({a}) == b({b})")

for i in range(1, 11):
    print(i * i)

