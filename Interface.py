# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(722, 269)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 10, 511, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.Time_duplicate = QtWidgets.QTextEdit(self.centralwidget)
        self.Time_duplicate.setGeometry(QtCore.QRect(20, 110, 201, 41))
        self.Time_duplicate.setReadOnly(True)
        self.Time_duplicate.setObjectName("Time_duplicate")
        self.row_duplicate = QtWidgets.QTextEdit(self.centralwidget)
        self.row_duplicate.setGeometry(QtCore.QRect(260, 110, 91, 41))
        self.row_duplicate.setReadOnly(True)
        self.row_duplicate.setObjectName("row_duplicate")
        self.column_duplicate = QtWidgets.QTextEdit(self.centralwidget)
        self.column_duplicate.setGeometry(QtCore.QRect(390, 110, 91, 41))
        self.column_duplicate.setReadOnly(True)
        self.column_duplicate.setObjectName("column_duplicate")
        self.serial_duplicate = QtWidgets.QTextEdit(self.centralwidget)
        self.serial_duplicate.setGeometry(QtCore.QRect(520, 110, 151, 41))
        self.serial_duplicate.setReadOnly(True)
        self.serial_duplicate.setObjectName("serial_duplicate")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 80, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(290, 80, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(420, 80, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(520, 80, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.Confirm_ignore = QtWidgets.QPushButton(self.centralwidget)
        self.Confirm_ignore.setEnabled(False)
        self.Confirm_ignore.setGeometry(QtCore.QRect(260, 180, 151, 51))
        self.Confirm_ignore.setObjectName("Confirm_ignore")
        self.Change_button = QtWidgets.QPushButton(self.centralwidget)
        self.Change_button.setGeometry(QtCore.QRect(10, 170, 101, 41))
        self.Change_button.setObjectName("Change_button")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setEnabled(False)
        self.spinBox.setGeometry(QtCore.QRect(120, 170, 101, 31))
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(999999999)
        self.spinBox.setProperty("value", 130000)
        self.spinBox.setObjectName("spinBox")
        self.Confirm_button = QtWidgets.QPushButton(self.centralwidget)
        self.Confirm_button.setEnabled(False)
        self.Confirm_button.setGeometry(QtCore.QRect(120, 210, 101, 31))
        self.Confirm_button.setObjectName("Confirm_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Duplicate Detection Software"))
        self.label.setText(_translate("MainWindow", "Tracking Duplicate Issue for GammaSU "))
        self.label_2.setText(_translate("MainWindow", "Thời gian trùng"))
        self.label_3.setText(_translate("MainWindow", "Hàng"))
        self.label_4.setText(_translate("MainWindow", "Cột"))
        self.label_5.setText(_translate("MainWindow", "Serial Duplicate"))
        self.Confirm_ignore.setText(_translate("MainWindow", "Loại bỏ con hàng trùng"))
        self.Change_button.setText(_translate("MainWindow", "Change number"))
        self.Confirm_button.setText(_translate("MainWindow", "CONFIRM"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
