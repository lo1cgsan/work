"""
Trzeba doinstalować: libxcb-cursor0
"""
import sys
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtWidgets import QLabel, QGridLayout
from PyQt6.QtWidgets import QLineEdit, QPushButton, QHBoxLayout
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtWidgets import QRadioButton, QGroupBox

class Kalkulator(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.interfejs()
        self.opcja = ''

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

        self.ukladO = QHBoxLayout()
        for v in ('m/s => km/s', 'C => F'):
            self.radio = QRadioButton(v)
            self.ukladO.addWidget(self.radio)
        # self.ukladO.itemAt(0).widget().setChecked(True)
        self.ukladO.itemAt(0).widget().toggled.connect(self.ustawOpcje)
        self.ukladO.itemAt(1).widget().toggled.connect(self.ustawOpcje)

        self.grupaO = QGroupBox('Opcje')
        self.grupaO.setLayout(self.ukladO)
        self.grupaO.setObjectName('Radio')
        self.grupaO.setCheckable(True)
        ukladG = QHBoxLayout()
        ukladG.addWidget(self.grupaO)
        ukladT.addLayout(ukladG, 2, 0, 1, 3)

        konwertujB = QPushButton("&Konwertuj", self)
        koniecB = QPushButton("&Koniec", self)

        ukladH = QHBoxLayout()
        ukladH.addWidget(konwertujB)
        ukladH.addWidget(koniecB)
        ukladT.addLayout(ukladH, 3, 0, 1, 3)

        self.setLayout(ukladT)

        koniecB.clicked.connect(self.koniec)
        konwertujB.clicked.connect(self.dzialanie)
        #self.grupaO.clicked.connect(self.ustawOpcje)

        self.show()

    def ustawOpcje(self, wartosc):
        nadawca = self.sender()
        if wartosc:
            self.opcja = nadawca.text()
            QMessageBox.warning(self, "Opcja", "Wybrałeś: " + self.opcja, QMessageBox.StandardButton.Ok)

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