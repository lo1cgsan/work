class Stos:
    def __init__(self, w):
        self.w = w
        self.SP = -1
        self.stos = [None] * w
        self.rozmiar = 0
        
    def push(self, element):
        if self.rozmiar < self.w:
            self.SP += 1
            self.stos[self.SP] = element
            return True
        else:
            print("Stack overflow.")
            return False

    def pop(self):
        if self.SP > -1:
            element = self.stos[self.SP]
            self.stos[self.SP] = None
            self.SP -= 1
            return element
        else:
            print("Stack underflow.")
            return False

    def top(self):
        if self.SP > -1:
            return self.stos[self.SP]
        else:
            print("Stack underflow.")
            return False

    def czy_pusty(self):
        return self.SP < 0
        

def czy_operator(znak):
    return znak in '()+-*/%^'

def priorytet(znak):
    if znak == '(':
        return 0
    elif znak in '+-':
        return 1
    elif znak in '*/%':
        return 2
    elif znak == '^':
        return 3

def konwertuj_do_ONP(wyrazenie):
    stos = Stos(len(wyrazenie))
    wynik = ''

    for znak in wyrazenie:
        if not czy_operator(znak):
            wynik += znak
        elif znak == '(':
            stos.push(znak)
        elif znak == ')':
            while stos.top() != '(':
                el = stos.pop()
                print("Zjęte: ", el)
                wynik += el
            stos.pop()  # zdjęcie otwierającego nawiasu
        else: # operator +-/*^%
            while not stos.czy_pusty() and priorytet(stos.top()) >= priorytet(znak):
                wynik += stos.pop()
            stos.push(znak)
        print(stos.stos)
        
    while not stos.czy_pusty():
        wynik += stos.pop()
    
    print(wynik)

wyrazenie = "(3 + 7) * 2"
# 3 7 + 2 *
konwertuj_do_ONP(wyrazenie)
