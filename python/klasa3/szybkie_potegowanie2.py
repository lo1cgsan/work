#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  szybkie_potegowanie2.py
#

def dec2bin(liczba, p=2):
    lbin = []
    while liczba != 0:
        lbin.append(liczba % p)
        liczba = liczba // p
    lbin.reverse()
    return lbin


def poteguj2(x, k):
    k = dec2bin(k)
    k.reverse()
    print(k)
    p = x
    for i in range(len(k) - 2, -1, -1):
        if k[i]:
            p = p * p * x
        else:
            p = p * p
    return p


def main(args):
    k = int(input("Podaj wykładnik: "))
    x = float(input("Podaj podstawę: "))
    print(poteguj2(x, k))
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
