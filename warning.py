from PyQt5 import QtWidgets
from PyQt5 import QtCore

def ignore_complete():
    msg = QtWidgets.QMessageBox()
    #icon Critical,Warning,Information,Question
    msg.setIcon(QtWidgets.QMessageBox.Information)
    msg.setText("Ignore successfully")
    msg.exec_()   

def pop_up_warning():
    msg = QtWidgets.QMessageBox()
    #icon Critical,Warning,Information,Question

    msg.setIcon(QtWidgets.QMessageBox.Critical)
    msg.setWindowFlags(msg.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)
    msg.setText("Có sản phẩm bị trùng.Kiểm tra lại phần mềm Check Duplicate")
    msg.exec_()   


def pop_up_OK():  
    msg = QtWidgets.QMessageBox()
    #icon Critical,Warning,Information,Question

    msg.setIcon(QtWidgets.QMessageBox.Information)
    msg.setWindowFlags(msg.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)
    msg.setText("Không có mã laser trùng. Tiếp tục sử dụng")
    msg.exec_()   
    