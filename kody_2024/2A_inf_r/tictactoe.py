# tictactoe
import pygame as pg
# from pygame.examples.video import backgrounds


class Plansza:
    def __init__(self, szer):
        self.szer = szer
        self.surface = pg.display.set_mode(
            (szer * 3, szer * 3), 0, 32
        )
        pg.display.set_caption('Kółko i krzyżyk')
        self.pole_gry = [None] * 9

        pg.font.init()
        font_path = pg.font.match_font('arial')
        self.font = pg.font.Font(font_path, 48)

    def rysuj(self):
        background = (0, 0, 0)
        self.surface.fill(background)
        self.rysuj_plansze()
        self.rysuj_znaczniki()

        pg.display.update()

    def rysuj_plansze(self):
        for i in range(3):
            for j in range(3):
                pg.draw.rect(self.surface, (255, 255, 255),
                             pg.Rect((j * self.szer, i * self.szer),
                                     (self.szer, self.szer)), 1
                             )

    def rysuj_znaczniki(self):
        # self.pole_gry = ['o', None, 'x', None, None, 'o', 'x', None, None]
        for x in range(3):
            for y in range(3):
                znacznik = self.pole_gry[x + y * 3]
                if not znacznik:
                    continue

                srodek_x = x * self.szer + self.szer / 2
                srodek_y = y * self.szer + self.szer / 2

                self.rysuj_tekst(znacznik, (srodek_x, srodek_y))

    def rysuj_tekst(self, tekst, srodek, kolor=(180, 180, 180)):
        tekst = self.font.render(tekst, True, kolor)
        prost = tekst.get_rect()
        prost.center = srodek
        self.surface.blit(tekst, prost)

    def ruch_gracza(self, x, y):
        x //= self.szer
        y //= self.szer
        self.pole_gry[x + y * 3] = 'X'

class Gra:
    def __init__(self, szer):
        pg.init()
        self.fps_clock = pg.time.Clock()
        self.plansza = Plansza(szer)
        self.ai_ruch = False

    def run(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    return True
                if event.type == pg.MOUSEBUTTONDOWN:
                    if self.ai_ruch:
                        continue
                    x, y = pg.mouse.get_pos()
                    self.plansza.ruch_gracza(x, y)
                    self.ai_ruch = False

            self.plansza.rysuj()
            self.fps_clock.tick(15)

class Ai():
    def __init__(self, plansza):
        self.plansza = plansza

    def wykonaj_ruch(self):
        pole = None

        uklady_wygrane = [[2, 2, 0], [2, 0, 2], [0, 2, 2]]
        uklady_blokuje = [[1, 1, 0], [1, 0, 1], [0, 1, 1]]

    def sprawdz_pola(self, uklad, wygrany=0):
        wartosc = None

game = Gra(150)
game.run()
