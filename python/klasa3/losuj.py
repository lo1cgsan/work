#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  losuj.py
#  
from random import randint
from random import uniform

def main(args):
    for i in range(20):
        print(randint(0, 10), "", end="")

    print()

    for i in range(20):
        print(uniform(10, 20), "", end="")

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
