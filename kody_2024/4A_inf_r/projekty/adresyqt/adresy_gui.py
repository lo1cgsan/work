# Form implementation generated from reading ui file 'adresy.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(412, 384)
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.splitter = QtWidgets.QSplitter(parent=Form)
        self.splitter.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.splitter.setObjectName("splitter")
        self.btn_dodaj = QtWidgets.QPushButton(parent=self.splitter)
        self.btn_dodaj.setObjectName("btn_dodaj")
        self.btn_zapisz = QtWidgets.QPushButton(parent=self.splitter)
        self.btn_zapisz.setObjectName("btn_zapisz")
        self.btn_edytuj = QtWidgets.QPushButton(parent=self.splitter)
        self.btn_edytuj.setObjectName("btn_edytuj")
        self.btn_usun = QtWidgets.QPushButton(parent=self.splitter)
        self.btn_usun.setObjectName("btn_usun")
        self.gridLayout.addWidget(self.splitter, 1, 2, 1, 1)
        self.lbl_nazwa = QtWidgets.QLabel(parent=Form)
        self.lbl_nazwa.setObjectName("lbl_nazwa")
        self.gridLayout.addWidget(self.lbl_nazwa, 0, 0, 1, 1)
        self.txt_nazwa = QtWidgets.QLineEdit(parent=Form)
        self.txt_nazwa.setObjectName("txt_nazwa")
        self.gridLayout.addWidget(self.txt_nazwa, 0, 1, 1, 1)
        self.txt_adres = QtWidgets.QTextEdit(parent=Form)
        self.txt_adres.setObjectName("txt_adres")
        self.gridLayout.addWidget(self.txt_adres, 1, 1, 1, 1)
        self.lbl_adresy = QtWidgets.QLabel(parent=Form)
        self.lbl_adresy.setObjectName("lbl_adresy")
        self.gridLayout.addWidget(self.lbl_adresy, 1, 0, 1, 1)
        self.splitter_2 = QtWidgets.QSplitter(parent=Form)
        self.splitter_2.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.btn_poprz = QtWidgets.QPushButton(parent=self.splitter_2)
        self.btn_poprz.setObjectName("btn_poprz")
        self.btn_nast = QtWidgets.QPushButton(parent=self.splitter_2)
        self.btn_nast.setObjectName("btn_nast")
        self.gridLayout.addWidget(self.splitter_2, 2, 1, 1, 1)
        self.btn_koniec = QtWidgets.QPushButton(parent=Form)
        self.btn_koniec.setObjectName("btn_koniec")
        self.gridLayout.addWidget(self.btn_koniec, 2, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btn_dodaj.setText(_translate("Form", "Dodaj"))
        self.btn_zapisz.setText(_translate("Form", "Zapisz"))
        self.btn_edytuj.setText(_translate("Form", "Edytuj"))
        self.btn_usun.setText(_translate("Form", "Usuń"))
        self.lbl_nazwa.setText(_translate("Form", "Nazwa"))
        self.lbl_adresy.setText(_translate("Form", "Adresy"))
        self.btn_poprz.setText(_translate("Form", "Poprzedni"))
        self.btn_nast.setText(_translate("Form", "Następny"))
        self.btn_koniec.setText(_translate("Form", "Koniec"))