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


while True:

    OKNOGRY.fill((0, 0, 0))
    rysuj_plansze()
    rysuj_pole_gry()
    pygame.display.update()
