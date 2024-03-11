# punkt A
x1 = float(input("Podaj x1: "))
y1 = float(input("Podaj y1: "))
# punkt B
x2 = float(input("Podaj x2: "))
y2 = float(input("Podaj y2: "))
# punkt C
x3 = float(input("Podaj x3: "))
y3 = float(input("Podaj y3: "))

if (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1) == 0:
    print("Punkty współliniowe.")
else:
    print("Niewspółliniowe.")

