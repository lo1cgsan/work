class Punkt:
    def __init__(self, nazwa, x=0, y=0):
        self.nazwa = nazwa
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self.nazwa}({self.x},{self.y})'
