#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  najczestszy.py


def policz_elementy(lista):
    wystapienia = dict()

    for i in lista:
        licznik = 0
        if i not in wystapienia:
            for j in lista:
                if i == j:
                    licznik += 1
            wystapienia[i] = licznik

    print(wystapienia)
    maks = 0
    lmaks = 0
    for i, (k, w) in enumerate(wystapienia.items()):
        if w > maks:
            maks = w
            lmaks = k
    print(lmaks, maks)


def main(args):
    lista = [3, 3, 5, 6, 7, 7, 1, 1, 1]
    policz_elementy(lista)
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
