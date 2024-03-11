#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  zwieksz50.py
#  

def main(args):
    a = int(input('Podaj liczbę: '))
    a = a + 1
    while a <= 50:
        a = a + 1
        print(a)
    print("a=", a)

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
