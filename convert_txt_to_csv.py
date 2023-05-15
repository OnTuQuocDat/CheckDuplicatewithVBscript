import pandas as pd
import shutil
import os

def copy_txt_file():
    startfile = r'C:\Sonion\debug.txt'
    endfile = r'C:\Sonion\debug_copy.txt'
    if os.stat(startfile).st_size != 0:
        shutil.copyfile(startfile,endfile)

def convert_csv():
    read_file = pd.read_csv(r'C:\Sonion\debug.txt',sep='\s+',header=None)
    read_file.to_csv(r'C:\Sonion\debug.csv',index=None)

def convert_txt():
    with open ('C:\Sonion\debug.csv','r') as f_in, open('C:\Sonion\debug.txt','w') as f_out:
        content = f_in.read().replace(',',' ')
        f_out.write(content)
