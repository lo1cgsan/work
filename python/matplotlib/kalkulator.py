from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtWidgets import QLabel, QGridLayout, QLineEdit, QPushButton, QHBoxLayout
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtCore import Qt

class Kalkulator(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.interfejs()

    def interfejs(self):
        # etykiety
        e1 = QLabel("Liczba 1:", self)
        e2 = QLabel("Liczba 2:", self)
        e3 = QLabel("Wynik:", self)

        uklad = QGridLayout()
        uklad.addWidget(e1, 0, 0)
        uklad.addWidget(e2, 0, 1)
        uklad.addWidget(e3, 0, 2)

        self.l1 = QLineEdit()
        self.l2 = QLineEdit()
        self.wynik = QLineEdit()
        self.wynik.setReadOnly(True)
        self.wynik.setToolTip("Wpisz liczby i wybierz działanie...")

        uklad.addWidget(self.l1, 1, 0)
        uklad.addWidget(self.l2, 1, 1)
        uklad.addWidget(self.wynik, 1, 2)

        dodajBtn = QPushButton("&Dodaj", self)
        odejmijBtn = QPushButton("&Odejmij", self)
        dzielBtn = QPushButton("&D&ziel", self)
        mnozBtn = QPushButton("&Mnóż", self)
        koniecBtn = QPushButton("&Koniec", self)

        ukladH = QHBoxLayout()
        ukladH.addWidget(dodajBtn)
        ukladH.addWidget(odejmijBtn)
        ukladH.addWidget(dzielBtn)
        ukladH.addWidget(mnozBtn)

        uklad.addLayout(ukladH, 2, 0, 1, 3)
        uklad.addWidget(koniecBtn, 3, 2)

        koniecBtn.clicked.connect(self.koniec)
        dodajBtn.clicked.connect(self.dzialania)
        odejmijBtn.clicked.connect(self.dzialania)
        mnozBtn.clicked.connect(self.dzialania)
        dzielBtn.clicked.connect(self.dzialania)

        self.setLayout(uklad)

        self.setGeometry(20, 20, 300, 100)
        self.setWindowTitle("Prosty kalkulator")
        self.show()

    def koniec(self):
        self.close()

    def closeEvent(self, event):
        odp = QMessageBox.question(
            self, 'Komunikat',
            'Czy na pewno zamykasz?',
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, QMessageBox.StandardButton.No
        )
        if odp == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Escape:
            self.close()

    def dzialania(self):
        try:
            l1 = float(self.l1.text())
            l2 = float(self.l2.text())
            nadawca = self.sender()
            if nadawca.text() == "&Dodaj":
                wynik = l1 + l2
            elif warunek

            self.wynik.setText(str(wynik))
        except ValueError:
            QMessageBox.warning(self, 'Błąd', 'Błędne dane', QMessageBox.StandardButton.Ok)

import sys
app = QApplication(sys.argv)
okno = Kalkulator()
app.exec()