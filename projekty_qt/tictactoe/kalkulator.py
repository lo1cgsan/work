from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtWidgets import QLabel, QLineEdit, QPushButton, QComboBox
from PyQt6.QtWidgets import QGridLayout, QHBoxLayout
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtCore import Qt


class Kalkulator(QWidget):

    def __init__(self):
        super().__init__()

        label1 = QLabel('Liczba 1:')
        label2 = QLabel('Liczba 2:')
        label3 = QLabel('Wynik:')

        self.liczba1 = QLineEdit()
        self.liczba2 = QLineEdit()
        self.wynik = QLineEdit()

        dodajBtn = QPushButton('Dodaj', self)
        odejmijBtn = QPushButton('Odejmij', self)
        dzielBtn = QPushButton('Dziel', self)
        mnozBtn = QPushButton('Mnóż', self)
        koniecBtn = QPushButton('Koniec', self)

        self.lista_cmb = QComboBox()
        self.lista_cmb.addItems(['m', 'cm', 'cale', 'stopy'])

        ukladH = QHBoxLayout()
        ukladH.addWidget(dodajBtn)
        ukladH.addWidget(odejmijBtn)
        ukladH.addWidget(dzielBtn)
        ukladH.addWidget(mnozBtn)

        ukladT = QGridLayout()
        ukladT.addWidget(label1, 0, 0)
        ukladT.addWidget(label2, 0, 1)
        ukladT.addWidget(label3, 0, 2)
        ukladT.addWidget(self.liczba1, 1, 0)
        ukladT.addWidget(self.liczba2, 1, 1)
        ukladT.addWidget(self.wynik, 1, 2)
        ukladT.addLayout(ukladH, 2, 0, 1, 3)
        ukladT.addWidget(koniecBtn, 3, 0, 1, 3)
        ukladT.addWidget(self.lista_cmb, 4, 0, 1, 2)

        dodajBtn.clicked.connect(self.wykonaj_dzialanie)
        odejmijBtn.clicked.connect(self.wykonaj_dzialanie)
        mnozBtn.clicked.connect(self.wykonaj_dzialanie)
        dzielBtn.clicked.connect(self.wykonaj_dzialanie)
        koniecBtn.clicked.connect(self.koniec)

        #self.lista_cmb.currentIndexChanged.connect(self.zmiana_indeksu)
        self.lista_cmb.currentTextChanged.connect(self.zmiana_indeksu)

        self.setLayout(ukladT)
        self.setWindowTitle('Kalkulator')

    def zmiana_indeksu(self, i):
        print(i)

    def koniec(self):
        self.close()

    def closeEvent(self, a0):
        msg_odp = QMessageBox.question(self,
                              'Komunikat',
                              'Czy na pewno koniec?',
                              QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                              QMessageBox.StandardButton.No)
        if msg_odp == QMessageBox.StandardButton.Yes:
            a0.accept()
        else:
            a0.ignore()

    def keyPressEvent(self, a0):
        if a0.key() == Qt.Key.Key_Escape:
            self.close()

    def wykonaj_dzialanie(self):

        nadawca = self.sender()
        wynik = ''

        try:
            liczba1 = float(self.liczba1.text())
            liczba2 = float(self.liczba2.text())

            if nadawca.text() == 'Dodaj':
                wynik = liczba1 + liczba2
            elif nadawca.text() == 'Odejmij':
                wynik = liczba1 - liczba2
            elif nadawca.text() == 'Mnoz':
                wynik = liczba1 * liczba2
            else:
                # if liczba2 != 0
                try:
                    wynik = liczba1 / liczba2
                except ZeroDivisionError:
                    QMessageBox.warning(self, 'Błąd', 'Nie dziel przez zero!!', QMessageBox.StandardButton.Ok)

            self.wynik.setText(str(round(wynik, 3)))

        except ValueError:
            QMessageBox.warning(self, 'Błąd', 'Błędne dane!', QMessageBox.StandardButton.Ok)

app = QApplication([])
okno = Kalkulator()
okno.show()
app.exec()