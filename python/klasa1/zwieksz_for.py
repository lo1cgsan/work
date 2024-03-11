#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  zwieksz50.py
#  

def main(args):
    a = int(input('Podaj liczbę: '))
    b = 1
    for i in range(a):
        b = b + 1
        # print(i)
    print("b=", b)

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
