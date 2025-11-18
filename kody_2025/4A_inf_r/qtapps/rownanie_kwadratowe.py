import sys

import math
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtWidgets import QLabel, QGridLayout, QHBoxLayout, QMessageBox
from PyQt6.QtWidgets import QLineEdit, QPushButton


class Rkwadratowe(QWidget):
    def __init__(self):
        super().__init__()
        self.interfejs()

    def interfejs(self):
        etykieta1 = QLabel("współczynnik A:", self)
        etykieta2 = QLabel("współczynnik B:", self)
        etykieta3 = QLabel("współczynnik C:", self)
        etykieta4 = QLabel("pierwiastek 1:", self)
        etykieta5 = QLabel("pierwiastek 2:", self)

        ukladT = QGridLayout()
        ukladT.addWidget(etykieta1, 0, 0)
        ukladT.addWidget(etykieta2, 1, 0)
        ukladT.addWidget(etykieta3, 2, 0)
        ukladT.addWidget(etykieta4, 1, 3)
        ukladT.addWidget(etykieta5, 2, 3)

        self.A = QLineEdit(self)
        self.B = QLineEdit(self)
        self.C = QLineEdit(self)
        self.pierwiastek_1 = QLineEdit(self)
        self.pierwiastek_2 = QLineEdit(self)
        self.pierwiastek_1.readonly = True
        self.pierwiastek_2.readonly = True

        ukladT.addWidget(self.A, 0, 1)
        ukladT.addWidget(self.B, 1, 1)
        ukladT.addWidget(self.C, 2, 1)
        ukladT.addWidget(self.pierwiastek_1, 1, 4)
        ukladT.addWidget(self.pierwiastek_2, 2, 4)

        przycisk_rozwiaz = QPushButton("&Rozwiaz", self)
        przycisk_koniec = QPushButton("&Koniec", self)

        ukladH = QHBoxLayout()
        ukladH.addWidget(przycisk_rozwiaz)

        ukladT.addLayout(ukladH, 4, 0, 1, 5)
        ukladT.addWidget(przycisk_koniec, 5, 0, 1, 5)

        przycisk_koniec.clicked.connect(self.koniec)
        przycisk_rozwiaz.clicked.connect(self.dzialanie)

        self.setLayout(ukladT)
        self.setGeometry(50, 50, 600, 100)
        self.setWindowTitle("Równanie kwadratowe")
        self.show()

    def dzialanie(self):
        nadawca = self.sender()
        try:
            A = int(self.A.text())
            B = int(self.B.text())
            C = int(self.C.text())

            if nadawca.text() == "&Rozwiaz":

                delta = (B*B) - (4*A*C)
                pierwiastek_z_delty = math.sqrt(delta)

                pierwiastek_1 = (-B + pierwiastek_z_delty)/ (2*A)
                pierwiastek_2 = (-B - pierwiastek_z_delty) / (2 *A)


            self.pierwiastek_1.setText(str(pierwiastek_1))
            self.pierwiastek_2.setText(str(pierwiastek_2))


        except ValueError:
            QMessageBox.warning(self, "Błąd", "Błędne dane (dla podanych współczynników delta jest UJEMNA. Brak pierwiastków!", QMessageBox.StandardButton.Ok)

    def koniec(self):
        self.close()

    def closeEvent(self, event):

        msg_box = QMessageBox()
        msg_box.setWindowTitle('Komunikat')
        msg_box.setText('Czy na pewno chcesz zakończyć program?')
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
okno = Rkwadratowe()
sys.exit(app.exec())