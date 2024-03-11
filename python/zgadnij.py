#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

def losuj(ile, maksliczba):
    liczby = []
    # i = 3
    # for i in range(3):
    while ile > 0:
        print(ile)
        liczba = random.randint(1, maksliczba)
        if liczba not in liczby:
            liczby.append(liczba)
            ile = ile - 1
    print(liczby)


def suma(ile):
    wynik = 0
    for i in range(ile):
        liczba = int(input("Podaj liczbę: "))
        wynik = wynik + liczba
    print("Suma liczb:", wynik)


def main(args):
    # losuj(3, 10)
    # losuj(5, 25)
    suma(5)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
