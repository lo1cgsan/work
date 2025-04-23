class Stos:
    def __init__(self):
        self.stos = []

    def push(self, element):
        self.stos.append(element)

    def pop(self):
        if self.empty():
            return self.stos.pop()
        else:
            print('Stos pusty')

    def empty(self):
        return len(self.stos)

def main():
    stos = Stos()
    stos.push(4)
    stos.push(5)
    stos.push('+')

    print(stos.pop())
    print(stos.pop())
    print(stos.pop())
    print(stos.pop())
