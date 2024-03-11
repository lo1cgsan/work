class Punkt:
    def __init__(self, nazwa, x=0, y=0):
        self.nazwa = nazwa
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"{self.nazwa}({self.x}, {self.y})"

def pobierzPunkty(punkty, nazwy):
    for n in nazwy:
        p = Punkt(n)
        p.x = float(input(f"Punkt {n}, podaj x: "))
        p.y = float(input(f"Punkt {n}, podaj y: "))
        punkty.append(p)

def czy_na_prostej(a, b, c):
    return (b.x - a.x) * (c.y - a.y) == (b.y - a.y) * (c.x - a.x)

def main():
    punkty = []
    pobierzPunkty(punkty, "ABC")
    a, b, c = punkty
    print(a, b, c)


main()
