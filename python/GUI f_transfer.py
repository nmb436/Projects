import shutil
import os
import datetime
from datetime import timedelta
from datetime import date
from datetime import datetime
import time
from tkinter import *
from tkinter import ttk


class FileTransfer:
    def __init__(self,master):
           
    
        #frame to hold widgets
        self.frame = ttk.Frame(root)
        self.frame.grid()
        self.frame.config(relief = RIDGE, padding = (30,15))

        #title for program
        self.label_title = ttk.Label(self.frame, text = 'Program to Transfer New Files to Destination Folder').grid(row=0, columnspan=3)

        #source and destination label, button, entry frame
        self.label_source = ttk.Label(self.frame, text = 'Source').grid(row = 1, column = 0)
        self.button_source = ttk.Button(self.frame, text ='find directory', command = self.askSource).grid(row = 1, column = 1)
        self.entry_source = Entry(self.frame).grid(row = 1, column = 2)

        self.label_destination = ttk.Label(self.frame, text = 'Destination').grid(row = 2, column = 0)
        self.button_destination = ttk.Button(self.frame, text ='find directory', command = self.askDestination).grid(row = 2, column = 1)
        self.entry_destination = Entry(self.frame).grid(row = 2, column = 2)

        #go button to execute file transfer
        self.label_go = ttk.Label(self.frame, text = 'transfer files').grid(row = 4, column = 1)
        self.button_go = ttk.Button(self.frame, text ='GO', command = self.file_transfer).grid(row = 4, column = 2)



    def askSource(self):
        source = tkFileDialog.askdirectory()
        return source

    def askDestination(self):
        destination = tkFileDialog.askdirectory()
        return destination


    def file_transfer(self):
        for file in os.listdir(source):
            last_date_modified = datetime.fromtimestamp(os.path.getmtime(source + file))
            now = datetime.now()
            time = (now - last_date_modified)
            time_range = timedelta(days=1)
            
            if  time <= time_range:
                
                shutil.move(source + file,destination)
                print(file)    
           

if __name__ == '__main__':
    root = Tk()
    app = FileTransfer(root)
    root.title('Gui for_ File Transfer') 
    root.mainloop()
    
