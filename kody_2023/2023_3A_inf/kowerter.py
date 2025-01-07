"""
Trzeba doinstalować: libxcb-cursor0
"""
import sys
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtWidgets import QLabel, QGridLayout
from PyQt6.QtWidgets import QLineEdit, QPushButton, QHBoxLayout
from PyQt6.QtWidgets import QMessageBox
# from PyQt6.QtWidgets import QRadioButton, QGroupBox
from PyQt6.QtWidgets import QComboBox, QCheckBox

class Kalkulator(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.interfejs()
        self.opcja = ''

    def interfejs(self):
        self.etykieta1 = QLabel("Wartość:", self)
        self.etykieta3 = QLabel("Wynik:", self)

        ukladT = QGridLayout()
        ukladT.addWidget(self.etykieta1, 0, 0)
        ukladT.addWidget(self.etykieta3, 0, 2)

        self.liczba1 = QLineEdit()
        self.wynik = QLineEdit()
        self.wynik.setReadOnly(True)

        ukladT.addWidget(self.liczba1, 1, 0)
        ukladT.addWidget(self.wynik, 1, 2)

        # self.ukladO = QHBoxLayout()
        # for v in ('m/s => km/h', 'C => F'):
        #     self.radio = QRadioButton(v)
        #     self.ukladO.addWidget(self.radio)
        # # self.ukladO.itemAt(0).widget().setChecked(True)
        # self.ukladO.itemAt(0).widget().toggled.connect(self.ustawOpcje)
        # self.ukladO.itemAt(1).widget().toggled.connect(self.ustawOpcje)
        #
        # self.grupaO = QGroupBox('Opcje')
        # self.grupaO.setLayout(self.ukladO)
        # self.grupaO.setObjectName('Radio')
        # self.grupaO.setCheckable(True)
        # ukladG = QHBoxLayout()
        # ukladG.addWidget(self.grupaO)
        # ukladT.addLayout(ukladG, 2, 0, 1, 3)

        listaK = QComboBox(self)
        konwersje = ['', 'm/s => km/h', 'C => F', 'h => s']
        for v in konwersje:
            listaK.addItem(v)
        listaK.textActivated[str].connect(self.ustawOpcje)
        ukladT.addWidget(listaK, 2, 0)

        odwroc = QCheckBox('Odwróć', self)
        odwroc.stateChanged.connect(self.zamienOpcje)
        ukladT.addWidget(odwroc, 2, 1, 1, 2)


        konwertujB = QPushButton("&Konwertuj", self)
        koniecB = QPushButton("&Koniec", self)

        ukladH = QHBoxLayout()
        ukladH.addWidget(konwertujB)
        ukladH.addWidget(koniecB)
        ukladT.addLayout(ukladH, 3, 0, 1, 3)

        self.setLayout(ukladT)

        koniecB.clicked.connect(self.koniec)
        konwertujB.clicked.connect(self.dzialanie)
        # self.grupaO.clicked.connect(self.ustawOpcje)

        self.show()

    def ustawOpcje(self, wartosc):
        # nadawca = self.sender()
        if wartosc:
            # self.opcja = nadawca.text()
            self.opcja = wartosc
            etykiety = self.opcja.split(' => ')
            self.etykieta1.setText(etykiety[0])
            self.etykieta3.setText(etykiety[1])
            # QMessageBox.warning(self, "Opcja", "Wybrałeś: " + self.opcja, QMessageBox.StandardButton.Ok)

    def zamienOpcje(self, stan):
        pass

    def koniec(self):
        self.close()

    def dzialanie(self):
        opcja_z = self.etykieta1.text()
        opcja_d = self.etykieta3.text()
        try:
            liczba1 = float(self.liczba1.text())
            wynik = ""

            if opcja_z == "m/s" and opcja_d == "km/h":
                pass
            elif opcja_z == "C" and opcja_d == "F":
                pass
            elif opcja_z == "h" and opcja_d == "s":
                pass

            self.wynik.setText(str(wynik))

        except ValueError:
            QMessageBox.warning(self, "Błąd", "Błędne dane!", QMessageBox.StandardButton.Ok)

app = QApplication(sys.argv)
okno = Kalkulator()
sys.exit(app.exec())