import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget
from adresy_gui import Ui_Form
from baza import polacz, czytaj_dane, wyswietl_komunikat, wykonaj_zapytanie
from enum import Enum

class Adresy(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(Adresy, self).__init__(parent)
        self.setupUi(self)

        self.setWindowTitle("Prosta książka adresowa")
        self.tryb = Enum('tryb', 't_dodaj t_edytuj t_nawiguj')
        self.aktualizuj_gui(self.tryb.t_dodaj)

        self.btn_koniec.clicked.connect(self.zakoncz)
        self.btn_dodaj.clicked.connect(self.dodaj)
        self.btn_zapisz.clicked.connect(self.zapisz)
        self.btn_edytuj.clicked.connect(self.edytuj)
        self.btn_nast.clicked.connect(self.nast)
        self.btn_poprz.clicked.connect(self.poprz)

        self.kontakty = []
        self.kontakty = czytaj_dane()
        print(self.kontakty)
        if self.kontakty:
            kontakt = self.pobierz_kontakt('', 0)
            print('Kontakt:', kontakt)
            self.txt_nazwa.setText(kontakt[0][0])
            self.txt_adres.setText(kontakt[0][1])
            self.aktualizuj_gui(self.tryb.t_nawiguj)

        self.indeks = 0
        self.stara_nazwa = ''
        self.stary_adres = ''
        self.t = self.tryb.t_dodaj

    def nast(self):
        if len(self.kontakty) <= 1:
            return
        nazwa = self.txt_nazwa.text()
        indeks = self.pobierz_kontakt(nazwa)
        kontakt = self.pobierz_kontakt('', indeks+1)
        self.txt_nazwa.setText(kontakt[0][0])
        self.txt_adres.setText(kontakt[0][1])

    def poprz(self):
        # sprawdź czy jest więcej niż 1 kontakt
        pass

    def zapisz(self):
        nazwa = self.txt_nazwa.text()
        adres = self.txt_adres.toPlainText()

        # sprawdzenie poprawności
        if nazwa.strip() == '' or adres.strip() == '':
            wyswietl_komunikat('Błąd danych!', 'Puste pola')
            return

        if self.t == self.tryb.t_dodaj:
            if self.pobierz_kontakt(nazwa) is None:
                self.kontakty.append({nazwa: adres})
                zapytanie = 'INSERT INTO adresy(nazwa, adres) VALUES(?, ?)'
                if wykonaj_zapytanie(zapytanie, (nazwa, adres)):
                    wyswietl_komunikat('Hurra', 'Jesteśmy w SPA!')
        elif self.t == self.tryb.t_edytuj:
            if self.stara_nazwa != nazwa:
                if self.pobierz_kontakt(nazwa) is None:
                    i = self.pobierz_kontakt(self.stara_nazwa)
                    del self.kontakty[i]  # usunięcie dotychczasowego kontaktu
                    self.kontakty.append({nazwa: adres})

                    zapytanie = 'UPDATE adresy SET nazwa = ?, adres = ? WHERE nazwa = ?'
                    if wykonaj_zapytanie(zapytanie, (nazwa, adres, self.stara_nazwa)):
                        wyswietl_komunikat('Hurra', 'Jesteśmy w SPA!')
                else:
                    wyswietl_komunikat('Ouu', 'Nazwa w słowniku!')
            elif self.stary_adres != adres:
                i = self.pobierz_kontakt(self.stara_nazwa)
                self.kontakty[i][nazwa] = {nazwa: adres}

                zapytanie = 'UPDATE adresy SET adres = ? WHERE nazwa = ?'
                if wykonaj_zapytanie(zapytanie, (adres, self.stara_nazwa)):
                    wyswietl_komunikat('Hurra', 'Jesteśmy w SPA!')

        self.aktualizuj_gui(self.tryb.t_nawiguj)

    def pobierz_kontakt(self, nazwa, index=None):
        for klucz, wartosc in enumerate(self.kontakty):
            if index is None:
                if wartosc.get(nazwa):
                    return klucz
            elif klucz == index:
                return list(wartosc.items())
        # jeżeli kontaktu nie ma
        return None

    def dodaj(self):
        self.stara_nazwa = self.txt_nazwa.text()
        self.stary_adres = self.txt_adres.toPlainText()
        self.txt_nazwa.clear()
        self.txt_adres.clear()

        self.aktualizuj_gui(self.tryb.t_dodaj)

    def edytuj(self):
        self.stara_nazwa = self.txt_nazwa.text()
        self.stary_adres = self.txt_adres.toPlainText()
        self.aktualizuj_gui(self.tryb.t_edytuj)

    def usun(self):
        pass

    def aktualizuj_gui(self, tryb):
        self.t = tryb
        if tryb == self.tryb.t_dodaj or tryb == self.tryb.t_edytuj:
            self.txt_nazwa.setReadOnly(False)
            self.txt_adres.setReadOnly(False)
            self.txt_nazwa.setFocus()
            self.btn_zapisz.show()
            self.btn_nast.setEnabled(False)
            self.btn_poprz.setEnabled(False)
            self.btn_edytuj.setEnabled(False)
            self.btn_usun.setEnabled(False)
            if tryb == self.tryb.t_edytuj:
                self.btn_dodaj.hide()
        elif tryb == self.tryb.t_nawiguj:
            print('Nawigacja')
            ile = len(self.kontakty)
            self.btn_dodaj.show()
            self.btn_dodaj.setEnabled(True)
            self.btn_edytuj.setEnabled(ile >= 1)
            self.btn_usun.setEnabled(ile >= 1)
            self.btn_nast.setEnabled(ile > 1)
            self.btn_poprz.setEnabled(ile > 1)

    def keyPressEvent(self, a0):
        if a0.key() == Qt.Key.Key_Escape:
            self.txt_nazwa.setText(self.stara_nazwa)
            self.txt_adres.setText(self.stary_adres)
            self.aktualizuj_gui(self.tryb.t_nawiguj)

    def zakoncz(self):
        self.close()

app = QApplication([])
if not polacz():
    sys.exit(1)

okno = Adresy()
okno.show()
app.exec()