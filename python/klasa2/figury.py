#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  figury.py
#  
import math


def licz_pole_prostokata():
    a = int(input("Podaj bok 1: "))
    b = int(input("Podaj bok 1: "))
    pole = a * b
    print(f"Pole wynosi: {pole}.")


def licz_obwod_prostokata(a, b):
    # a = int(input("Podaj bok 1: "))
    # b = int(input("Podaj bok 1: "))
    obwod = a * b
    print(f"Obwód wynosi: {obwod}.")


def licz_pole_kola():
    r = float(input("Podaj promień: "))
    pole = math.pi * r**2
    print(f"Pole wynosi: {pole}.")


def main(args):
    # a = int(input("Podaj bok 1: "))
    # b = int(input("Podaj bok 1: "))
    # licz_pole_prostokata()
    # licz_obwod_prostokata(a, b)
    licz_pole_kola()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
