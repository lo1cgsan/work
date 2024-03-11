from math import sqrt

a = float(input("Podaj a: "))
b = float(input("Podaj b: "))
c = float(input("Podaj c: "))

if a == 0:
    print("Błędne dane!")
else:
    d = b**2 - 4 * a * c

    if d < 0:
        print("Brak rozwiązań!")
    elif d == 0:
        x = -b / 2 * a
        print(x, a * x**2 + b * x + c)
    else:
        x1 = (-b - sqrt(d)) / 2 * a
        x2 = (-b + sqrt(d)) / 2 * a
        print(x1, a * x1**2 + b * x1 + c)
        print(x2, a * x2**2 + b * x2 + c)
