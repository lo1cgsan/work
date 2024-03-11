class Stos:
    def __init__(self, w):
        self.stos = [None] * w
        self.rozmiar = 0
        
    def push(self, element):
        if self.rozmiar < w:
            SP += 1
            stos[SP] = element
            return True
        else:
            print("Stack overflow.")
            return False

    def pop(self):
        if SP > -1:
            element = stos[SP]
            SP -= 1
            return element
        else:
            print("Stack underflow.")
            return False


def main():
    stos = [None] * w
    push(stos, 10)
    push(stos, 20)
    push(stos, 30)
    
    print(pop(stos))
    print(pop(stos))
    print(pop(stos))
    
main()
