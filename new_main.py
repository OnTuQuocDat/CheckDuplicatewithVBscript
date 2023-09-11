# Author: On Tu Quoc Dat - Control System Engineer
# Company : Sonion Viet Nam Co.,Ltd
# Version : 1.1
# Update: 27/04/2023
# Built = Python 3.10.7 

#Special command python -m PyQt5.uic.pyuic -x Interface.ui -o Interface.py



from PyQt5.QtWidgets import QApplication,QMainWindow,QLineEdit
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
import csv
import os

global csv_direct

csv_direct = "debug.csv"
txt_direct = "debug.txt"
file_txt_name = "output.txt"
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
        read_file = open("number_file.txt","r")
        self.memorydata = int(read_file.read())
        self.page1.spinBox.setValue(self.memorydata)
        
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

        #self.win1.close()
        #exit()

    def action_confirmbutton(self):
        change_number_complete()
        #Save data to number_file.txt
        with open("number_file.txt", "w") as file:
            file.write(self.page1.spinBox.text())

        self.page1.spinBox.text()
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
        serial0 = data['0'].to_list()
        serial1 = data['1'].to_list()
        serial2 = data['2'].to_list()
        serial4 = data['4'].to_list()
        serial6 = data['6'].to_list()
        # print(serial)
        # print("Row 1: ",serial1[100],serial[100])
        return serial,serial0,serial1,serial2,serial4,serial6
    
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
        #print("Unique: ",unique_duplicates)
        #print("Length List check: ",len(list_serial))

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
            max_value.append(min(save_dup['Dup' +str(i)]))

        print("MAX VALUE: ",max_value)

        # print("Dup1: ",max(save_dup['Dup'+str(0)]))
        # print("Dup2: ",max(save_dup['Dup'+str(1)]))

        return max_value, len(unique_duplicates)

    def find_index_father_file(self,row):
        with open(txt_direct,'r') as file:
            lines = file.readlines()
            try:
                index = lines.index(row + '\n')
                print(f"The index of the row '{row}' is: {index}")
            except ValueError:
                print(f"The row '{row}' was not found in the file.")
                index = 0
        return index

    def delete_line(self,file_path,index):
        with open(file_path,'r') as file:
            lines = file.readlines()
        modified_lines = []
        for line_number, line in enumerate(lines):
            if line_number != index:
                modified_lines.append(line)
        
        with open(file_path,'w') as file:
            file.writelines(modified_lines)

    def display_ui(self,position_duplicate,colum0,colum1,colum2,colum4,colum6,list_check):
        # self.data = pd.read_csv(csv_direct)
        display_ui_date = colum0[position_duplicate]
        display_ui_time = colum1[position_duplicate]
        display_ui_AMPM = colum2[position_duplicate]
        display_ui_row = colum4[position_duplicate]
        display_ui_column = colum6[position_duplicate]
        display_ui_serial = list_check[position_duplicate]
        # display_ui_date = self.data.iat[position_duplicate,0] #Hàng 5 cột 0
        # display_ui_time = self.data.iat[position_duplicate,1]
        # display_ui_AMPM = self.data.iat[position_duplicate,2]
        # display_ui_row = self.data.iat[position_duplicate,4]
        # display_ui_column = self.data.iat[position_duplicate,6]
        # display_ui_serial = self.data.iat[position_duplicate,7]
        
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
        self.list_check = []
        self.list_check_col0 = []
        self.list_check_col1 = []
        self.list_check_col2 = []
        self.list_check_col4 = []
        self.list_check_col6 = []
        self.list_father_check = []
    def main_thread(self):
        print("Process 1 lan") 
        #Full data in debug txt file
        serial_number,colum0,colum1,colum2,colum4,colum6 = run_algorithm.relation_csv_to_list() #LIST TOTAL
        #06/09/2023
        if int(w.page1.spinBox.text()) <= len(serial_number):
            final_end = int(w.page1.spinBox.text())
        else:
            final_end = len(serial_number)
        for i in range(1,final_end):  #LIST CHECK
            self.list_check.append(serial_number[-i])
            self.list_check_col0.append(colum0[-i])
            self.list_check_col1.append(colum1[-i])
            self.list_check_col2.append(colum2[-i])
            self.list_check_col4.append(colum4[-i])
            self.list_check_col6.append(colum6[-i])
        #print(self.list_check)
        # if len(serial_number) < int(w.page1.spinBox.text()):
        #     print("Chua du data,cu tiep tuc", len(serial_number))
        # else:
        #     print("Qua nhieu data roi, delete di")

        #     delete_half = int(w.page1.spinBox.text())/2
        #     delete_half = int(delete_half)
        #     for i in range(0,delete_half):
        #         del serial_number[i]
                

        #Write data to csv saving file
        # with open ('output.csv','w',newline='') as file:
        #     writer = csv.writer(file)
        #     writer.writerow(['Date','Time','AMPM','ROWS','COLUMN','Serial'])
        #     for i in range(len(self.list_check)):
        #         writer.writerow([colum0[i],colum1[i],colum2[i],colum4[i],colum6[i],self.list_check[i]])

        #Write data to txt saving file
        
        file = open(file_txt_name,'w')
        for i in range(len(self.list_check)):
            file.write(str(self.list_check_col0[i]) + ' '+ str(self.list_check_col1[i]) + ' '+str(self.list_check_col2[i]) + ' '+'ROWS'+ ' '+str(self.list_check_col4[i]) + ' '+'COLUMN'+' '+str(self.list_check_col6[i]) + ' '+str(self.list_check[i]) + '\n')
        file.close()
        ##########
        # index_duplicate,w.len_duplicate = run_algorithm.find_duplicates(serial_number)
        index_duplicate,w.len_duplicate = run_algorithm.find_duplicates(self.list_check)
        print("Len duplicate: ",w.len_duplicate)
        print("Index duplicate: ",index_duplicate)
        if w.len_duplicate == 0:
            w.close_window.emit()

        if w.len_duplicate > 0:
            w.popup_window.emit()
            for w.index_dup in index_duplicate:
                w.wait_val = 0
                run_algorithm.display_ui(w.index_dup,self.list_check_col0,self.list_check_col1,self.list_check_col2,self.list_check_col4,self.list_check_col6,self.list_check)
                father_row_to_find = str(self.list_check_col0[w.index_dup]) + ' ' + str(self.list_check_col1[w.index_dup]) + ' ' + str(self.list_check_col2[w.index_dup]) + ' ' + 'ROWS' + ' '+str(self.list_check_col4[w.index_dup]) + ' '+'Column'+' '+str(self.list_check_col6[w.index_dup]) + ' '+str(self.list_check[w.index_dup])
                print("Father row to find: ",father_row_to_find)
                total_index = run_algorithm.find_index_father_file(father_row_to_find)
                self.list_father_check.append(total_index)
                print("List father file: ",self.list_father_check)
                w.setText_example.emit()
                w.wait_val = 1
                while w.wait_val == 1:
                    pass
            print("Xoa file")
            #delete_lines('output.csv',index_duplicate)

            #Delete file child
            #Open the file in read mode and read all the lines into a list
            with open(file_txt_name,'r') as file:
                lines = file.readlines()
            #Use a loop to remove the rows from the list
            for index in sorted(index_duplicate, reverse=True):
                del lines[index]
            #Open the same file in write mode and write the updated list to the file
            with open(file_txt_name,'w') as file:
                file.writelines(lines)

            #Find index list file father

            #Delete file father
            with open(txt_direct,'r') as father_file:
                father_lines = father_file.readlines()
            #Use a loop to remove the rows from the list
            for father_index in sorted(self.list_father_check, reverse=True): ####################################IN CHARGE
                del father_lines[father_index]
            with open(txt_direct,'w') as father_file:
                father_file.writelines(father_lines)
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