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

    def uruchom(self):
        """ Główna pętla programu """
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            self.plansza.rysuj()


class ObiektGraf:
    """ Klasa bazowa """

    def __init__(self, szer, wys, x, y, kolor=(0, 255, 0)):
        self.szer, self.wys = szer, wys
        self.kolor = kolor
        self.pow = pygame.Surface(
            [szer, wys], pygame.SRCALPHA, 32
        )
        self.pow.convert_alpha()
        # toDo


if __name__ == "__main__":
    gra = PongGra(800, 400)
    gra.uruchom()
