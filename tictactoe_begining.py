#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
import sys
import random
from pygame.locals import *

pygame.init()

OKNOGRY = pygame.display.set_mode((300, 300), 0, 32)
pygame.display.set_caption('Kółko i krzyżyk')

POLE_GRY = [0, 0, 0,
            0, 0, 0,
            0, 0, 0]
RUCH = 1  # do kogo należy ruch, 1 - gracz, 0 - komputer
WYGRANY = 0  # 0 - nikt, 1 - gracz, 2 - komputer, 3 - remis
WYGRANA = False


def rysuj_plansze():
    for i in range(3):
        for j in range(3):
            pygame.draw.rect(OKNOGRY, (255, 255, 255),
                             Rect((j * 100, i * 100), (100, 100)), 1)


def rysuj_pole_gry():
    for i in range(3):
        for j in range(3):
            pole = i * 3 + j  # 0, 1, 2, ..., 8
            x = j * 100 + 50  # 25, 75, 125
            y = i * 100 + 50  # 25, 25, 25

            if POLE_GRY[pole] == 1:
                pygame.draw.circle(OKNOGRY, (0, 0, 255), (x, y), 45)
            elif POLE_GRY[pole] == 2:
                pygame.draw.circle(OKNOGRY, (255, 0, 0), (x, y), 45)


def postaw_znak(pole, RUCH):
    if POLE_GRY[pole] == 0:
        if RUCH == 1:  # ruch gracza
            POLE_GRY[pole] = 1
            return 2
        elif RUCH == 2:  # ruch komputera
            POLE_GRY[pole] = 2
            return 1
    return RUCH


def sprawdz_pola(uklad, wygrany=None):
    wartosc = None
    POLA_INDEKSY = [  # trójki pól do sprawdzenia
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # poziom
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # pion
        [0, 4, 8], [2, 4, 6]  #na ukos
    ]

    for lista in POLA_INDEKSY:
        kol = []  # lista pomocnicza
        for ind in lista:
            kol.append(POLE_GRY[ind])
        if (kol in uklad):
            wartosc = wygrany if wygrany else lista[kol.index(0)]

    return wartosc


def ai_ruch(RUCH):
    pole = None

    uklady_wygrywam = [[2, 2, 0], [2, 0, 2], [0, 2, 2]]
    uklady_blokuje = [[1, 1, 0], [1, 0, 1], [0, 1, 1]]

    pole = sprawdz_pola(uklady_wygrywam)
    if pole is not None:
        return postaw_znak(pole, RUCH)

    pole = sprawdz_pola(uklady_blokuje)
    if pole is not None:
        return postaw_znak(pole, RUCH)

    while pole is None:
        pos = random.randrange(0, 9)
        if POLE_GRY[pos] == 0:
            pole = pos

    return postaw_znak(pole, RUCH)


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if WYGRANA is False:
            if RUCH == 1:
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        mouseX, mouseY = event.pos
                        pole = (int(mouseY / 100) * 3) + int(mouseX / 100)
                        RUCH = postaw_znak(pole, RUCH)
            elif RUCH == 2:
                RUCH = ai_ruch(RUCH)

    OKNOGRY.fill((0, 0, 0))
    rysuj_plansze()
    rysuj_pole_gry()
    pygame.display.update()
