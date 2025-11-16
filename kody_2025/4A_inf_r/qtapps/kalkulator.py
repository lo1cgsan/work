import sys
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtWidgets import QLabel, QGridLayout, QHBoxLayout, QMessageBox
from PyQt6.QtWidgets import QLineEdit, QPushButton

class Kalkulator(QWidget):
    def __init__(self):
        super().__init__()
        self.interfejs()

    def interfejs(self):
        etykieta1 = QLabel("Liczba 1:", self)
        etykieta2 = QLabel("Liczba 2:", self)
        etykieta3 = QLabel("wynik:", self)

        ukladT = QGridLayout()
        ukladT.addWidget(etykieta1, 0, 0)
        ukladT.addWidget(etykieta2, 0, 1)
        ukladT.addWidget(etykieta3, 0, 2)

        self.liczba_1 = QLineEdit(self)
        self.liczba_2 = QLineEdit(self)
        self.wynik = QLineEdit(self)
        self.wynik.readonly = True
        self.wynik.setToolTip('Wpisz liczby i wybierz działanie.')

        ukladT.addWidget(self.liczba_1, 1, 0)
        ukladT.addWidget(self.liczba_2, 1, 1)
        ukladT.addWidget(self.wynik, 1, 2)

        przycisk_dodaj = QPushButton("Dodaj", self)
        przycisk_odejmij = QPushButton("Odejmij", self)
        przycisk_mnoz = QPushButton("Mnóż", self)
        przycisk_dziel = QPushButton("Dziel", self)
        przycisk_koniec = QPushButton("Koniec", self)

        ukladH = QHBoxLayout()
        ukladH.addWidget(przycisk_dodaj)
        ukladH.addWidget(przycisk_odejmij)
        ukladH.addWidget(przycisk_dziel)
        ukladH.addWidget(przycisk_mnoz)

        ukladT.addLayout(ukladH, 2, 0, 1, 3)
        ukladT.addWidget(przycisk_koniec, 3, 0, 1, 3)

        przycisk_koniec.clicked.connect(self.koniec)
        przycisk_dodaj.clicked.connect(self.dzialanie)
        przycisk_odejmij.clicked.connect(self.dzialanie)
        przycisk_dziel.clicked.connect(self.dzialanie)
        przycisk_mnoz.clicked.connect(self.dzialanie)

        self.setLayout(ukladT)
        self.setGeometry(20, 20, 300, 100)
        self.setWindowTitle("Kalkulator")
        self.show()

    def dzialanie(self):
        nadawca = self.sender()
        try:
            liczba1 = float(self.liczba_1.text())
            liczba2 = float(self.liczba_2.text())
            if nadawca.text() == "Dodaj":
                wynik = liczba1 + liczba2
            elif nadawca.text() == "Odejmij":
                wynik = liczba1 - liczba2
            elif nadawca.text() == "Mnóż":
                wynik = liczba1 * liczba2
            else:  # dzielenie
                try:
                    wynik = round(liczba1 / liczba2, 9)
                except ZeroDivisionError:
                    QMessageBox.critical(
                        self, "Błąd", "Nie można dzielić przez zero!")
                    return
            self.wynik.setText(str(wynik))
        except ValueError:
            QMessageBox.warning(self, "Błąd", "Błędne dane", QMessageBox.StandardButton.Ok)

    def koniec(self):
        self.close()

    def closeEvent(self, event):

        msg_box = QMessageBox()
        msg_box.setWindowTitle('Komunikat')
        msg_box.setText('Czy na pewno koniec?')
        msg_box.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        msg_box.setDefaultButton(QMessageBox.StandardButton.No)
        odp = msg_box.exec()
        if odp == QMessageBox.StandardButton.Yes.value:
            event.accept()
        else:
            event.ignore()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key.Key_Escape:
            self.close()


app = QApplication([])
okno = Kalkulator()
sys.exit(app.exec())