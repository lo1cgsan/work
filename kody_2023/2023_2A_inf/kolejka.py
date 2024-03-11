class Kolejka:
    def __init__(self, w):
        self.w = w
        self.SP = -1
        self.tablica = [None] * w
        self.rozmiar = 0
        
    def push(self, element):
        if self.rozmiar < self.w:
            self.SP += 1
            self.tablica[self.SP] = element
            return True
        else:
            print("Stack overflow.")
            return False

    def pop(self):
        if self.SP > -1:
            element = self.tablica[self.SP]
            self.tablica[self.SP] = None
            self.SP -= 1
            return element
        else:
            print("Stack underflow.")
            return False

    def top(self):
        if self.SP > -1:
            return self.tablica[self.SP]
        else:
            print("Stack underflow.")
            return False

    def czy_pusty(self):
        return self.SP < 0
