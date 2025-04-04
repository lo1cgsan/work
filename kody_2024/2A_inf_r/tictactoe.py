# tictactoe
import random

import pygame as pg
# from pygame.examples.video import backgrounds


class Plansza:
    def __init__(self, szer):
        self.szer = szer
        self.surface = pg.display.set_mode(
            (szer * 3, szer * 3), 0, 32
        )
        pg.display.set_caption('Kółko i krzyżyk')
        self.pole_gry = [0] * 9

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
        tekst = self.font.render(str(tekst), True, kolor)
        prost = tekst.get_rect()
        prost.center = srodek
        self.surface.blit(tekst, prost)

    def ruch_gracza(self, x, y):
        x //= self.szer
        y //= self.szer
        self.pole_gry[x + y * 3] = 1

    def sprawdz_pola(self, uklad, wygrany=0):
        wartosc = None
        # lista wielowymiarowa
        POLA_INDEKSY = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # indeksy pól w poziomie (wiersze)
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # indeksy pól w pionie (kolumny)
            [0, 4, 8], [2, 4, 6]  # przekątne
        ]

        for lista in POLA_INDEKSY:
            l_pom = []
            for i in lista:
                l_pom.append(self.pole_gry[i])
            if l_pom in uklad:
                # zwróć wygranego (1, 2) lub indeks pola do zaznaczenia
                wartosc = wygrany if wygrany else lista[l_pom.index(0)]

        return wartosc

class Gra:
    def __init__(self, szer):
        pg.init()
        self.fps_clock = pg.time.Clock()
        self.plansza = Plansza(szer)
        self.ai = Ai(self.plansza)
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
                    self.ai_ruch = True

            self.plansza.rysuj()

            if self.ai_ruch:
                self.ai.wykonaj_ruch(self.plansza.pole_gry)
                self.ai_ruch = False

            self.fps_clock.tick(15)

    def czy_jest_wygrany(self):
        pass

    def wypisz_tekst(self):
        pass

class Ai():
    def __init__(self, plansza):
        self.plansza = plansza

    def wykonaj_ruch(self, pole_gry):
        pole = None

        uklady_wygrane = [[2, 2, 0], [2, 0, 2], [0, 2, 2]]
        uklady_blokuje = [[1, 1, 0], [1, 0, 1], [0, 1, 1]]

        pole = self.plansza.sprawdz_pola(uklady_wygrane)
        if pole is not None:
            pole_gry[pole] = 2
            return

        pole = self.plansza.sprawdz_pola(uklady_blokuje)
        if pole is not None:
            pole_gry[pole] = 2
            return

        while pole is None:
            pos = random.randint(0, 8)
            if self.plansza.pole_gry[pos] == 0:
                pole = pos

        pole_gry[pole] = 2

game = Gra(150)
game.run()
