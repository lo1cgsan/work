from stos import Stos

class ONP(Stos):
    def __init__(self, o_str):
        super().__init__()
        self.o_str = o_str.strip()
        self.a_str = ''
        self.wynik = None

# 2 7 + 3 / 14 3 − 4 × + 2 /