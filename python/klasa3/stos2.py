#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Stos:
    def __init__(self):
        self.elementy = []
    
    def push(self, element):
        self.elementy.append(element)

    def pop(self):
        return self.elementy.pop()

    def size(self):
        return len(self.elementy)

    def empty(self):
        return len(self.elementy)

stos = Stos()
if stos.empty():
    print("stos coś zawiera")
else:
    print("stos pusty jest")

stos.push(4)
stos.push('dog')
stos.push(True)
print(stos.size())
print(stos.pop())
print(stos.pop())
print(stos.size())
if stos.empty():
    print("stos coś zawiera")
