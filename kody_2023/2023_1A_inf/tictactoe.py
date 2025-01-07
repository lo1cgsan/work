import pygame as pg
import sys

pg.init()
SZER = 80

PLANSZA = pg.display.set_mode((SZER * 3, SZER * 3), 0, 32)
pg.display.set_caption('Kółko i krzyżyk')

# 0 – pole puste, 1 – gracz, 2 – komputer
POLE_GRY = [0, 0, 0,
            0, 0, 0,
            0, 0, 0]

def rysuj_plansze():
    for i in range(3):
        for j in range(3):
            pg.draw.rect(PLANSZA, (255, 255, 255),
                         pg.Rect((j * SZER, i * SZER), (SZER, SZER)), 1)


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    PLANSZA.fill((0, 0, 0))
    rysuj_plansze()
    pg.display.update()
