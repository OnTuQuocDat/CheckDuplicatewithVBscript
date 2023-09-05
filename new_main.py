# Author: On Tu Quoc Dat - Control System Engineer
# Company : Sonion Viet Nam Co.,Ltd
# Version : 1.1
# Update: 27/04/2023
# Built = Python 3.10.7 

#Special command python -m PyQt5.uic.pyuic -x Interface.ui -o Interface.py



from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.QtCore import QThread,QObject,pyqtSignal,QRunnable,pyqtSlot
from PyQt5 import QtWidgets,QtCore
import sys
import datetime
from time import strftime,localtime
import pandas as pd
from Interface import Ui_MainWindow
from Password import Ui_PasswordWindow
from convert_txt_to_csv import *
from time import sleep
from warning import *
import shutil
import time
#global trigger_auto

global csv_direct
global_password = "IDEE"
csv_direct = "debug.csv"
txt_direct = "debug.txt"

class Password_page(QMainWindow):
    def __init__(self):
        super().__init__()
        self.winpass = QMainWindow()
        self.page2 = Ui_PasswordWindow()
        self.page2.setupUi(self.winpass)
        self.winpass.setFixedHeight(166)
        self.winpass.setFixedWidth(513)
        self.winpass.show()

        self.page2.Enter_password.clicked.connect(self.check_password)

    def check_password(self):
        if self.page2.password_blank.text() == "admin":
            print("pass")
            #Enable button set dung lượng file
            w.page1.spinBox.setEnabled(True)
            w.page1.Confirm_button.setEnabled(True)
            self.winpass.close()

            
            
        else:
            wrong_password()
            self.winpass.close()


class Page1(QMainWindow):
    setText_example = pyqtSignal()
    close_window = pyqtSignal()
    close_all = pyqtSignal()
    popup_window = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.win1 = QMainWindow()
        self.page1 = Ui_MainWindow()
        self.page1.setupUi(self.win1)
        self.win1.setFixedHeight(269)
        self.win1.setFixedWidth(722)
        self.setText_example.connect(self.test)
        self.close_window.connect(self.close_page1)
        self.close_all.connect(self.close_program)
        self.popup_window.connect(self.display_for_OP)
        self.wait_val = 1
        self.win1.show()
        self.display_datetime = None
        self.display_row = None
        self.display_column = None
        self.display_serial = None
        self.len_duplicate = 0 

        self.page1.Confirm_ignore.clicked.connect(self.delete_duplicate)

        self.page1.Change_button.clicked.connect(self.change_datafile)
        
        self.page1.Confirm_button.clicked.connect(self.action_confirmbutton)

    @pyqtSlot()
    def display_for_OP(self):
        pop_up_warning()

    @pyqtSlot()
    def close_program(self):
        self.win1.close()
        #exit()

    @pyqtSlot()
    def close_page1(self):
        pop_up_OK()
        self.win1.close()
        #exit()

    def action_confirmbutton(self):
        change_number_complete()
        self.page1.spinBox.setEnabled(False)
        self.page1.Confirm_button.setEnabled(False)


    def change_datafile(self):
        self.winpass = Password_page()
    
    def delete_duplicate(self):
        ignore_complete()
        self.setText_example.emit()
        self.display_datetime = None
        self.display_row = None
        self.display_column = None
        self.display_serial = None 
        self.page1.Time_duplicate.setText("")
        self.page1.row_duplicate.setText("")
        self.page1.column_duplicate.setText("")
        self.page1.serial_duplicate.setText("")
        # data = pd.read_csv("debug_copy.csv")
        # data_save = data.drop(labels=[self.index_dup],axis=0)
        # data_save.to_csv("debug.csv",index=False)

        self.page1.Confirm_ignore.setEnabled(False)
        self.wait_val = 0

    @pyqtSlot()
    def test(self):
        # pop_up_warning()
        self.page1.Time_duplicate.setText(self.display_datetime)
        self.page1.row_duplicate.setText(str(self.display_row))
        self.page1.column_duplicate.setText(str(self.display_column))
        self.page1.serial_duplicate.setText(self.display_serial)
        self.page1.Confirm_ignore.setEnabled(True)
        
class BackEnd(QMainWindow):
    def __init__(self):
        super().__init__()
        self.trigger_auto = 0
        self.trigger_check = 0
             


    def relation_csv_to_list(self):
        #copy_txt_file() #DAQ edit 12/5/2023
        convert_csv()
        #Get cot thu 8 in to list python
        ##Dat ten cho column
        # column_names = ["Date","Time","AMPM","ROWS","numROW","COLUMN","numColumn","Serial"]
        # df = pd.read_csv("debug.csv",names=column_names)
        # test = df.coul
        data = pd.read_csv(csv_direct)
        # self.copy_data = data.copy()
        # self.copy_data.to_csv("debug_copy.csv",index=False)
        serial = data['7'].to_list()
        # print(serial)
        return serial#,self.copy_data
    
    def seperate_file(self):
        #Cut 25k line đầu to backup file theo giờ
        pass
    

    def delete_seperate_file(self):
        pass


    def find_duplicates(self,list_serial):
        duplicates = []
        for number in list_serial:
            if list_serial.count(number) > 1:
                duplicates.append(number) 
        #duplicates = [number for number in list_serial if list_serial.count(number) > 1]
        unique_duplicates = list(set(duplicates))
        # if len(unique_duplicates) > 0:
        #     pop_up_warning()
        

        #
        indices = []
        for (index,item) in enumerate(list_serial):
            for test in unique_duplicates:
                if item == test:
                    indices.append(index)
        #

        save_dup = {}
        max_value = []
        for i in range (0,len(unique_duplicates)):
            save_dup['Dup' +str(i)] = []
        # print(save_dup['Dup1'])
            for j in range(0,len(list_serial)):
                # for k in range(0,len(unique_duplicates)):
                if list_serial[j] == unique_duplicates[i]:
                    # print("List serial: ",[j])
                    # print("List unique duplicate: ",[i])
                    save_dup['Dup'+str(i)].append(j)
            max_value.append(max(save_dup['Dup' +str(i)]))
        print("MAX VALUE: ",max_value)

        # print("Dup1: ",max(save_dup['Dup'+str(0)]))
        # print("Dup2: ",max(save_dup['Dup'+str(1)]))

        return max_value, len(unique_duplicates)




    def display_ui(self,position_duplicate):
        self.data = pd.read_csv(csv_direct)

        display_ui_date = self.data.iat[position_duplicate,0] #Hàng 5 cột 0
        display_ui_time = self.data.iat[position_duplicate,1]
        display_ui_AMPM = self.data.iat[position_duplicate,2]
        display_ui_row = self.data.iat[position_duplicate,4]
        display_ui_column = self.data.iat[position_duplicate,6]
        display_ui_serial = self.data.iat[position_duplicate,7]
        
        w.display_datetime = str(display_ui_date + display_ui_time + display_ui_AMPM)
        w.display_row = str(display_ui_row)
        w.display_column = str(display_ui_column)
        w.display_serial = str(display_ui_serial)



class Worker1(QObject):
    finished1 = pyqtSignal()
    progress1 = pyqtSignal(int)
    gui_display = pyqtSignal()
    def __init__(self):
        super().__init__()
    def main_thread(self):
        print("Process 1 lan") 
        #Full data in debug txt file
        serial_number = run_algorithm.relation_csv_to_list()
        
        index_duplicate,w.len_duplicate = run_algorithm.find_duplicates(serial_number)
        data = pd.read_csv(csv_direct)
        print("Len duplicate: ",w.len_duplicate)

        if w.len_duplicate == 0:
            w.close_window.emit()

        if w.len_duplicate > 0:
            w.popup_window.emit()
            for w.index_dup in index_duplicate:
                w.wait_val = 0
                run_algorithm.display_ui(w.index_dup)

                w.setText_example.emit()
                w.wait_val = 1
                while w.wait_val == 1:
                    pass

            #Đợi xác nhận hết rồi Xoa du lieu luôn 1 lần
            # for delete_index in index_duplicate:
            #     data = data.drop(labels=[delete_index],axis=0)
            # data.to_csv(csv_direct,index=False)

            # #Xóa trên txt, hoàn tất process
            # print("INDEX DUPLICATE: ",index_duplicate)


            # a_file = open(txt_direct,"r")
            # lines = a_file.readlines()
            # a_file.close()
            # #delete rows
            # for i in range(0,len(index_duplicate)):
            #     del lines[index_duplicate[i]]
            #     # print("Line thu: ", i)
            #     # print(lines[index_duplicate[i]])
            # #write to new file
            # new_file = open(txt_direct,"w+")
            # for line in lines:
            #     new_file.write(line)
            # new_file.close()

            #Open the file in read mode and read all the lines into a list
            with open(txt_direct,'r') as file:
                lines = file.readlines()
            #Use a loop to remove the rows from the list
            for index in sorted(index_duplicate, reverse=True):
                del lines[index]
            #Open the same file in write mode and write the updated list to the file
            with open(txt_direct,'w') as file:
                file.writelines(lines)
            w.close_all.emit()
            
def change_number_complete():
    msg = QtWidgets.QMessageBox()
    #icon Critical,Warning,Information,Question
    msg.setIcon(QtWidgets.QMessageBox.Information)
    msg.setText("Complete change")
    msg.exec_()          

def wrong_password():
    msg = QtWidgets.QMessageBox()
    #icon Critical,Warning,Information,Question
    msg.setIcon(QtWidgets.QMessageBox.Warning)
    msg.setText("Wrong Password")
    msg.exec_()   

if __name__ == '__main__':
    try:     
        app = QApplication(sys.argv)

        thread1 = QThread()
        worker_1 = Worker1()
        worker_1.moveToThread(thread1)
        
        w = Page1()
        run_algorithm = BackEnd()


        thread1.started.connect(worker_1.main_thread)
        worker_1.finished1.connect(thread1.quit)
        worker_1.finished1.connect(thread1.deleteLater)
        thread1.finished.connect(thread1.deleteLater)
        thread1.start()


        sys.exit(app.exec())

        
    except KeyboardInterrupt:
        print("Error")