import sys
from PyQt6.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import QRect


class Tabela(QWidget):

    def __init__(self, szer):
        super().__init__()

        self.szer = szer
        self.A = []
        self.P = []
        self.n = 0
        self.m = 0
        self.kroki = None
        self.koniec = False
        self.nr_wiersza = 0

        self.pobierz_dane()

    def pobierz_dane(self):
        with open('dane.txt') as plik:
            for i, wiersz in enumerate(plik):
                if i == self.nr_wiersza:
                    dane = wiersz.strip().split(' ')
                    self.n, self.m = int(dane.pop(0)), int(dane.pop(0))
                    dane = list(map(int, dane))

                    self.A = [ dane[i:i + self.m] for i in range(0, len(dane), self.m) ]
                    self.P = self.A
                    self.kroki = self.wykonaj_krok()
                    return

            self.koniec = True

    def wykonaj_krok(self):
        self.P = [ [None for _ in range(self.m)] for _ in range(self.n) ]
        self.P[0][0] = True

        for i in range(self.n):
            for j in range(self.m):
                if self.A[i][j] == 0:
                    self.P[i][j] = False
                else:
                    # jeżeli 1 wiersz i nie 1 kolumna
                    if i == 0 and j > 0:
                        self.P[i][j] = self.P[i][j - 1]
                    # jeżeli nie 1 wiersz i 1 kolumna
                    if i > 0 and j == 0:
                        self.P[i][j] = self.P[i - 1][j]
                    # jeżeli nie 1 wiersz i nie 1 kolumna
                    if i > 0 and j > 0:
                        self.P[i][j] = self.P[i][j - 1] or self.P[i - 1][j]
                print(self.P)
                yield  # generator

    def paintEvent(self, a0):
        self.setFixedSize(self.szer * self.m + 2, self.szer * self.n + 2)
        qp = QPainter()
        qp.begin(self)
        self.rysuj_tabele(qp)
        qp.end()

    def rysuj_tabele(self, qp):
        kolor_o = QColor(0, 0, 0)

        for i in range(self.n):
            for j in range(self.m):
                kolor_w = QColor(0, 0, 0)
                if self.P[i][j] is None:
                    kolor_w = QColor(100,100,100)
                elif self.P[i][j]:
                    kolor_w = QColor(255, 255, 255)

                qp.setPen(kolor_o)
                qp.setBrush(kolor_w)

                # prost = QRect(j * self.szer, i * self.szer, self.szer, self.szer)
                # qp.drawRect(prost)
                qp.drawEllipse(j * self.szer, i * self.szer, self.szer, self.szer)

    def mousePressEvent(self, a0):
        try:
            next(self.kroki)
        except StopIteration:
            if not self.koniec:
                self.nr_wiersza += 1
                self.pobierz_dane()
            else:
                QMessageBox.information(
                    self,
                    'Informacja',
                    'Brak danych!',
                    QMessageBox.StandardButton.Yes
                )
                self.close()
        self.update()


app = QApplication([])
okno = Tabela(100)
okno.show()
sys.exit(app.exec())

