#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  szybkie_potegowanie.py

def dec2bin(liczba):
    tab = []
    while liczba != 0:
        tab.append(liczba % 2)
        liczba = liczba // 2
    tab.reverse()
    return tab


def poteguj_szybko(x, k):
    k = dec2bin(k)
    print(k)
    p = x
    k.reverse()
    # 4(2) = [0, 0, 1]
    for i in range(len(k) - 2, -1, -1):
        if k[i] == 1:
            p = p * p * x
        else:
            p = p * p
    return p


def main(args):
    # k = int(input("Podaj wykładnik: "))
    # x = fliczbaoat(input("Podaj podstawę: "))
    # print(f"{x}^{k} = {poteguj_szybko(x, k)}")
    assert(poteguj_szybko(2, 3) == 8)
    assert(poteguj_szybko(3, 2) == 9)
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
