class Osoba:
    def __init__(self, imie, nazwisko, pesel):
        self.imie = imie
        self.nazwisko = nazwisko
        if self.sprawdz_pesel(pesel):
            self.pesel = pesel
        else:
            self.pesel = ''

    def sprawdz_pesel(self, pesel):
        return True

    def __str__(self):
        return self.imie + ' ' + self.nazwisko


class Konto:
    def __init__(self, osoba, ile=0):
        self.osoba = osoba
        self.bilans = ile

    def wplata(self, ile):
        self.bilans += ile

    def wyplata(self, ile):
        self.bilans -= ile

    def pobierz_kwote(self, komunikat):
        print(komunikat)
        ile = float(input("Podaj kwotę: "))
        return ile

    def wypisz_bilans(self):
        print(self.bilans)

class KontoMinimum(Konto):
    def __init__(self, osoba, ile, bilans_min):
        Konto.__init__(self, osoba, ile)
        self.bilans_min = bilans_min

    def wyplata(self, ile):
        if self.bilans - ile < self.bilans_min:
            print('Brak środków.')
        else:
            Konto.wyplata(self, ile)

class Samochod():
    def __init__(self, marka, model, rok, osoba):
        self.marka = marka
        self.model = model
        self.rok_produkcji = rok
        self.wlasciciel = osoba


o1 = Osoba('Jan', 'Kowalski', '1234567890')
print(o1)

print()
b = KontoMinimum(o1, 100, -100)
print(b.osoba)
b.wypisz_bilans()
b.wyplata(1000)
b.wypisz_bilans()
