from math import sqrt

d = float(input("Podaj przekątną: "))

while d <= 0:
    print("Przekątna musi być większa od zera!")
    d = float(input("Podaj przekątną: "))

if d > 0:
    a = d / sqrt(3)
    pole = a**2 * 6
    v = a**3

    print(f"Pole: {round(pole, 2)}\nObjętość: {round(v, 2)}")
else:
    print("Błędne dane!")
