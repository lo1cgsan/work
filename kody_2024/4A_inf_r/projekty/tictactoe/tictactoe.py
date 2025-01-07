import pygame as pg
import sys


class Plansza:
    def __init__(self, szer):
        self.szer = szer
        self.surface = pg.display.set_mode((szer * 3, szer * 3), 0, 32)

        self.pole_gry = [None] * 9
        self.A = [[1,  1, 1], [0, 1, 0], [1,  1, 1]]
        self.P = [[None,  None, None], [None,  None, None], [None,  None, None]]

    def rysuj(self, *args):
        self.surface.fill((0, 0, 0))
        self.rysuj_plansze()
        # self.rysuj_pole()

        pass

        pg.display.update()

    def rysuj_plansze(self):
        for i in range(3):
            for j in range(3):
                kolor = (0, 0, 0)
                if self.tb_wej[i][j]:
                    kolor = (255, 255, 255)
                pg.draw.rect(self.surface, kolor,
                             pg.Rect(j * self.szer, i * self.szer, self.szer - 2, self.szer - 2))


    def wykonaj_krok(self):
        for i in range(n):
            for j in range(m):
                # i = 2, j = 2
                if A[i][j] == 0:
                    P[i][j] = False
                else:
                    # jeżeli 1 wiersz i nie 1 kolumna
                    if i == 0 and j > 0:
                        P[i][j] = P[i][j - 1]
                    # jeżeli nie 1 wiersz i 1 kolumna
                    if i > 0 and j == 0:
                        P[i][j] = P[i - 1][j]
                    # jeżeli nie 1 wiersz i nie 1 kolumna
                    if i > 0 and j > 0:
                        P[i][j] = P[i][j - 1] or P[i - 1][j]

class Gra:
    def __init__(self, szer):
        pg.init()
        self.plansza = Plansza(szer)

    def run(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

            self.plansza.rysuj()


gra = Gra(100)
gra.run()