from stos import Stos

class ONP(Stos):
    def __init__(self, o_str):
        super().__init__()
        self.o_str = o_str.strip()
        self.wynik = None

    def oblicz_onp(self):
        onp = self.o_str.split(" ")
        for wyraz in onp:
            if wyraz.isdigit():
                self.push(wyraz)
                # print(wyraz)
            else:
                a = self.pop()
                b = self.pop()
                wartosc = b wyraz a
                print(b, wyraz, a)

onp1 = ONP('2 7 + 3 / 14 3 − 4 × + 2 /')
onp1.oblicz_onp()

onp2 = ONP('2 3 + 5 ×')
onp2.oblicz_onp()
