#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  kolory.py
import random


def losuj():
    kolory = ['red', 'green', 'blue', 'cyan', 'magenta', 'yellow']
    for jola in range(3):
        print(kolory[random.randint(0, 5)])


def main(args):
    for jola in range(3):
        losuj()

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
