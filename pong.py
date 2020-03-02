#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
import sys
from pygame.locals import *

OKNOGRY_SZER = 800
OKNOGRY_WYS = 400
KOLOR_BLUE = (230, 255, 255)

oknogry = pygame.display.set_mode((OKNOGRY_SZER, OKNOGRY_WYS), 0, 32)
pygame.display.set_caption('Prosty Pong')

P_SZER = 100
P_WYS = 20
BLUE = (0, 0, 255)

P1_POZ = [350, 350]
paletka1 = pygame.Surface([P_SZER, P_WYS])
paletka1.fill(BLUE);
paletka1_prost = paletka1.get_rect()
paletka1_prost.x = P1_POZ[0]
paletka1_prost.y = P1_POZ[1]

P2_POZ = [350, 20]
paletka2 = pygame.Surface([P_SZER, P_WYS])
paletka2.fill(BLUE);
paletka2_prost = paletka2.get_rect()
paletka2_prost.x = P2_POZ[0]
paletka2_prost.y = P2_POZ[1]
PREDKOSC_AI = 5

PI_SZER = 20
PI_WYS = 20
PI_VX = 6
PI_VY = 6
GREEN = (0, 255, 0)
pilka = pygame.Surface([PI_SZER, PI_WYS], pygame.SRCALPHA, 32)
pilka.convert_alpha()
pygame.draw.ellipse(pilka, GREEN, [0, 0, PI_SZER, PI_WYS])

pilka_prost = pilka.get_rect()
pilka_prost.x = OKNOGRY_SZER / 2
pilka_prost.y = OKNOGRY_WYS / 2

FPS = 30
fpsClock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == MOUSEMOTION:
            myszaX, myszaY = event.pos

            przesuniecie = myszaX - (P_SZER / 2)

            if przesuniecie > OKNOGRY_SZER - P_SZER:
                przesuniecie = OKNOGRY_SZER - P_SZER
            if przesuniecie < 0:
                przesuniecie = 0

            paletka1_prost.x = przesuniecie

    pilka_prost.move_ip(PI_VX, PI_VY)
    # jeżeli piłka wykracza poza pole gry
    # z lewej/prawej – odwracamy kierunek ruchu poziomego piłki
    if pilka_prost.right >= OKNOGRY_SZER:
        PI_VX *= -1
    elif pilka_prost.left <= 0:
        PI_VX *= -1

    if pilka_prost.top <= 0 or pilka_prost.bottom >= OKNOGRY_WYS:
        pilka_prost.x = OKNOGRY_SZER / 2
        pilka_prost.y = OKNOGRY_WYS / 2

    # jeżeli piłka dotknie paletki gracza
    if pilka_prost.colliderect(paletka1_prost):
        PI_VY *= -1
        # zapobiegaj przysłanianiu paletki przez piłkę
        pilka_prost.bottom = paletka1_prost.top

    # AI
    # jeżeli piłka ucieka na prawo, przesuń za nią paletkę
    if pilka_prost.centerx > paletka2_prost.centerx:
        paletka2_prost.x += PREDKOSC_AI
    # piłka ucieka na lewo
    elif pilka_prost.centerx < paletka2_prost.centerx:
        paletka2_prost.x -= PREDKOSC_AI

    # jeżeli piłka dotknie paletki AI
    if pilka_prost.colliderect(paletka2_prost):
        PI_VY *= -1
        pilka_prost.top = paletka2_prost.bottom

    oknogry.fill(KOLOR_BLUE)

    oknogry.blit(paletka1, paletka1_prost)
    oknogry.blit(paletka2, paletka2_prost)
    oknogry.blit(pilka, pilka_prost)

    pygame.display.update()
    fpsClock.tick(FPS)
