"""
Trzeba doinstalować: libxcb-cursor0
"""
import sys
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtWidgets import QLabel, QGridLayout
from PyQt6.QtWidgets import QLineEdit, QPushButton, QHBoxLayout
from PyQt6.QtWidgets import QMessageBox

class Kalkulator(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.interfejs()

    def interfejs(self):
        etykieta1 = QLabel("Liczba 1:", self)
        etykieta2 = QLabel("Liczba 2:", self)
        etykieta3 = QLabel("Wynik:", self)

        ukladT = QGridLayout()
        ukladT.addWidget(etykieta1, 0, 0)
        ukladT.addWidget(etykieta2, 0, 1)
        ukladT.addWidget(etykieta3, 0, 2)

        self.liczba1 = QLineEdit()
        self.liczba2 = QLineEdit()
        self.wynik = QLineEdit()
        self.wynik.setReadOnly(True)

        ukladT.addWidget(self.liczba1, 1, 0)
        ukladT.addWidget(self.liczba2, 1, 1)
        ukladT.addWidget(self.wynik, 1, 2)

        dodajB = QPushButton("&Dodaj", self)
        odejmijB = QPushButton("&Odejmij", self)
        dzielB = QPushButton("&Mnóż", self)
        mnozB = QPushButton("D&ziel", self)
        koniecB = QPushButton("&Koniec", self)

        ukladH = QHBoxLayout()
        ukladH.addWidget(dodajB)
        ukladH.addWidget(odejmijB)
        ukladH.addWidget(dzielB)
        ukladH.addWidget(mnozB)

        ukladT.addLayout(ukladH, 2, 0, 1, 3)
        ukladT.addWidget(koniecB, 4, 0, 1, 3)
        self.setLayout(ukladT)

        koniecB.clicked.connect(self.koniec)
        dodajB.clicked.connect(self.dzialanie)
        odejmijB.clicked.connect(self.dzialanie)
        dzielB.clicked.connect(self.dzialanie)
        mnozB.clicked.connect(self.dzialanie)

        self.show()

    def koniec(self):
        self.close()

    def dzialanie(self):
        nadawca = self.sender()

        try:
            liczba1 = float(self.liczba1.text())
            liczba2 = float(self.liczba2.text())
            wynik = ""

            if nadawca.text() == "&Dodaj":
                wynik = liczba1 + liczba2
            elif nadawca.text() == "&Odejmij":
                pass
            elif nadawca.text() == "&Mnóż":
                pass
            else:
                try:
                    wynik = round(liczba1 / liczba2, 9)
                except ZeroDivisionError:
                    QMessageBox.critical(self, "Błąd", "Nie można dzielić przez zero!")

            self.wynik.setText(str(wynik))

        except ValueError:
            QMessageBox.warning(self, "Błąd", "Błędne dane!", QMessageBox.StandardButton.Ok)

app = QApplication(sys.argv)
okno = Kalkulator()
sys.exit(app.exec())