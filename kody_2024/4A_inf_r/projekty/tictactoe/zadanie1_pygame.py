import pygame as pg
import sys


class Plansza:
    def __init__(self, szer, dane):
        self.szer = szer
        self.n = len(dane)  # liczba wierszy
        self.m = len(dane[0])  # liczbę kolumn

        self.surface = pg.display.set_mode((szer * self.m, szer * self.n), 0, 32)

        self.A = dane
        self.P = self.A
        self.kroki = self.wykonaj_krok()

    def rysuj(self):
        self.surface.fill((0, 0, 0))

        for i in range(self.n):
            for j in range(self.m):
                kolor = (0, 0, 0)
                if self.P[i][j] is None:
                    kolor = (100,100,100)
                elif self.P[i][j]:
                    kolor = (255, 255, 255)
                pg.draw.rect(self.surface, kolor,
                             (j * self.szer, i * self.szer, self.szer - 2, self.szer - 2))


    def wykonaj_krok(self):
        self.P = [ [None for _ in range(self.m)] for _ in range(self.n) ]
        self.P[0][0] = True

        for i in range(self.n):
            for j in range(self.m):
                if self.A[i][j] == 0:
                    self.P[i][j] = False
                else:
                    # jeżeli 1 wiersz i nie 1 kolumna
                    if i == 0 and j > 0:
                        self.P[i][j] = self.P[i][j - 1]
                    # jeżeli nie 1 wiersz i 1 kolumna
                    if i > 0 and j == 0:
                        self.P[i][j] = self.P[i - 1][j]
                    # jeżeli nie 1 wiersz i nie 1 kolumna
                    if i > 0 and j > 0:
                        self.P[i][j] = self.P[i][j - 1] or self.P[i - 1][j]
                print(self.P)
                yield  # generator


class Tabela:
    def __init__(self, szer, dane):
        pg.init()
        self.plansza = Plansza(szer, dane)
        self.fps_clock = pg.time.Clock()

    def run(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

                if event.type == pg.MOUSEBUTTONDOWN:
                    try:
                        next(self.plansza.kroki)
                    except StopIteration:
                        print("Koniec")

            self.plansza.rysuj()

            pg.display.update()
            self.fps_clock.tick(15)


with open('dane.txt') as plik:
    for wiersz in plik:
        dane = wiersz.strip().split(' ')
        n, m = int(dane.pop(0)), int(dane.pop(0))
        print(dane)
        dane = list(map(int, dane))
        dane2 = []
        for i in range(0, len(dane), m):
            dane2.append(dane[i:i+m])
        print(dane2)

        tab = Tabela(100, dane2)
        tab.run()
