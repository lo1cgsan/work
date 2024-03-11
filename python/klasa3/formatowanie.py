#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  formatowanie.py
import math


def main(args):
    a = 100
    b = 30
    print('%10.5f' % math.pi)
    print('liczba 1: {:>10} liczba 2: {:3d}'.format(a, b))
    print('{:10.5f}'.format(math.pi))
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
