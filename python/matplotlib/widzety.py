from PyQt6.QtWidgets import QApplication, QWidget
from gui import Ui_Widget


class Widgety(QWidget, Ui_Widget):
    """ Główna klasa aplikacji """

    def __init__(self, parent=None):
        super(Widgety, self).__init__(parent)
        self.setupUi(self)  # tworzenie interfejsu

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    okno = Widgety()
    okno.show()

    sys.exit(app.exec())