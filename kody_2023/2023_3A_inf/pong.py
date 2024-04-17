import pygame
from pygame.locals import *
import sys


class Plansza:
    def __init__(self, szer, wys):
        self.szer, self.wys = szer, wys
        self.pow = pygame.display.set_mode((szer, wys), 0, 32)
        pygame.display.set_caption('Mój Pong')

    def rysuj(self, *args):
        self.pow.fill((200, 255, 255))
        for obiekt in args:
            self.pow.blit(obiekt.pow, obiekt.prost)
        pygame.display.update()


class PongGra:
    """ Kontroler gry """

    def __init__(self, szer, wys):
        pygame.init()
        self.plansza = Plansza(szer, wys)
        self.pal1 = Paletka(100, 20, 350, 20, kolor=(255, 0, 0))
        self.pal2 = Paletka(100, 20, 350, 360, kolor=(0, 0, 255))
        self.pilka = Pilka(20, 20, 390, 190, kolor=(0, 255, 0), pv_x=6, pv_y=6)
        self.pilka2 = Pilka(20, 20, 390, 190, kolor=(0, 255, 100), pv_x=-6, pv_y=6)
        self.gracz_ui = GraczUI(self.pal1, self.pilka, 6)
        # zegar śledzący czas
        self.fps_zegar = pygame.time.Clock()

    def uruchom(self):
        """ Główna pętla programu """
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == MOUSEMOTION:
                    m_x, m_y = event.pos  # współrzędne kursora
                    self.pal2.przesun(m_x, self.plansza.szer)

            self.pilka.ruszaj(self.plansza.szer, self.plansza.wys,
                              self.pal1, self.pal2)
            self.pilka2.ruszaj(self.plansza.szer, self.plansza.wys,
                               self.pal1, self.pal2)
            self.gracz_ui.ruszaj()

            self.plansza.rysuj(
                self.pal1,
                self.pal2,
                self.pilka,
                self.pilka2
            )

            # ustaw prędkość animacji
            self.fps_zegar.tick(30)


class ObiektGraf:
    """ Klasa bazowa """

    def __init__(self, szer, wys, x, y, kolor=(0, 255, 0)):
        self.szer, self.wys = szer, wys
        self.kolor = kolor
        self.pow = pygame.Surface(
            [szer, wys], pygame.SRCALPHA, 32
        )
        self.pow.convert_alpha()
        self.prost = self.pow.get_rect(x=x, y=y)


class Paletka(ObiektGraf):
    def __init__(self, szer, wys, x, y, kolor=(0, 0, 255), maks_v=10):
        super().__init__(szer, wys, x, y, kolor)
        self.maks_v = maks_v
        self.pow.fill(self.kolor)

    def przesun(self, m_x, szer_p):
        przesuniecie = m_x - self.maks_v
        if przesuniecie > szer_p - self.szer:
            przesuniecie = szer_p - self.szer
        elif przesuniecie < 0:
            przesuniecie = 0
        self.prost.x = przesuniecie


class Pilka(ObiektGraf):
    def __init__(self, szer, wys, x, y, kolor=(255, 0, 0), pv_x=3, pv_y=3):
        super().__init__(szer, wys, x, y, kolor)
        pygame.draw.ellipse(self.pow, self.kolor, [0, 0, self.szer, self.wys])
        self.pv_x = pv_x
        self.pv_y = pv_y
        self.start_x = x
        self.start_y = y

    def ruszaj(self, szer_p, wys_p, *args):
        self.prost.move_ip(self.pv_x, self.pv_y)

        # piłka wykracza poza pole na lewo/prawo
        if self.prost.right >= szer_p or self.prost.left <= 0:
            self.pv_x *= -1

        # piłka uciekła na dół/górę
        if self.prost.top <= 0 or self.prost.bottom >= wys_p:
            self.prost.x = szer_p // 2
            self.prost.y = wys_p // 2

        for obj in args:
            if self.prost.colliderect(obj.prost):
                self.pv_y *= -1


class GraczUI:
    def __init__(self, pal, pilka, pal_v=6):
        self.pal = pal
        self.pilka = pilka
        self.pal_v = pal_v

    def ruszaj(self):
        # jeżeli piłka leci na prawo
        if self.pilka.prost.centerx > self.pal.prost.centerx:
            self.pal.prost.x += self.pal_v

        # jeżeli piłka leci w lewo
        elif self.pilka.prost.centerx < self.pal.prost.centerx:
            self.pal.prost.x -= self.pal_v


if __name__ == "__main__":
    gra = PongGra(800, 400)
    gra.uruchom()
