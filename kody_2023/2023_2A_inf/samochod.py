from osoba_klasa import Osoba


class Kierowca(Osoba):

    def __init__(self, imie, kategoria):
        super().__init__(imie)
        self.kategoria = kategoria


    def __str__(self):
        zwróć imię, płeć i kategorię


print(k1)