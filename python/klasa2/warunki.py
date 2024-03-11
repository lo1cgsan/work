#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  warunki.py

def czyTrojkat1(a, b, c):
    if a + b > c:
        print("1 warunek prawdziwy!")
        if a + c > b:
            print("1 i 2 warunek prawdziwy!")
            if b + c > a:
                print("1, 2 i 3 warunek prawdziwy!")
                print("Da się!")


def czyTrojkat2(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        print("1, 2 i 3 warunek prawdziwy!")
        print("Da się!")
    else:
        print("Nie da się!")


def main():
    a = int(input("Podaj 1. bok: "))
    b = int(input("Podaj 2. bok: "))
    c = int(input("Podaj 3. bok: "))
    czyTrojkat2(a, b, c)
    return 0


main()
