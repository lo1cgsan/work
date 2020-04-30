#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  licz_liczby.py
#
from biblioteka import losujLiczby, min, max


def ileLiczb():
    """
    Funkcja zlicza ilość wystąpień elementów w podanej
    liście.
    """
    pass


def main(args):
    tab = []  # pusta lista
    n = int(input("Ile liczb? "))
    MAKS = 20
    losujLiczby(tab, n, MAKS)
    print("Wylosowano: ", tab)

    # zlicz ilość wystąpień liczb
    # znajdź i wydrukuj liczby występujące
    # minimalną i maksymalną ilość razy
    
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
