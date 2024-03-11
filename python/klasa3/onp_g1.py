#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Stos:
    # LIFO
    stos = []
    
    def push(self, dane):
        self.stos.append(dane)
    
    def pop(self):
        return self.stos.pop()

# 4 6 3 - /
# 4,6,3
# 4,3
# 1.333

def main(args):
    stos = Stos()
    onp = input('Podaj wyrażenie ONP: ')
    operand = ''
    for znak in onp:
        print(ord(znak))
        if znak != " " and znak.isdigit():
            operand += znak
        elif znak == " " and len(operand):
            stos.push(operand)
            operand = ''
        elif znak in ('+', '-', '*' , '/', '%'):
            a = stos.pop()
            b = stos.pop()
            stos.push(eval(str(b) + znak + str(a)))
        else:
            print("Błędny znak!")
    print("Wynik: ", stos.pop())
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
