#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
import sys
import random
from pygame.locals import *

pygame.init()

SZER = 800
WYS = 400
OKNOGRY = pygame.display.set_mode((SZER, WYS), 0, 32)
pygame.display.set_caption('Moja gra')

x_kolo = int(50)
y_kolo = int(50)

kolo = pygame.Surface([100, 100], pygame.SRCALPHA, 32).convert_alpha()
pygame.draw.ellipse(kolo, (255, 0, 0), [0, 0, 100, 100])
kolo_prost = kolo.get_rect()
kolo_prost.x = 0
kolo_prost.y = 0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    OKNOGRY.fill((103, 226, 43))
    # pygame.draw.circle(OKNOGRY, (255, 0, 0), (x_kolo, y_kolo), 50)
    OKNOGRY.blit(kolo, kolo_prost)
    pygame.display.update()
