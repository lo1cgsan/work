#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  czynniki_rozklad.py

# 56 / 2 = 28, 2
# 28 / 2 = 14, 2
# 14 / 2 = 7, 2
# 7 / 7 = 1, 7
# 56 = 2 * 2 * 2 * 7

def rozloz_liczbe(n):
    czynniki = []  # pusta lista
    c = 2
    while n != 1:
        while n % c == 0:
            n = n // c
            czynniki.append(c)
        c = c + 1
    return czynniki


def main(args):
    n = int(input("Podaj liczbę: "))
    print(rozloz_liczbe(n))
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
