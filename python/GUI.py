import shutil
import os
import datetime
from datetime import timedelta
from datetime import date
from datetime import datetime
import time
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import sqlite3


class FileTransfer:
    def __init__(self,master):
           
    
        #frame to hold widgets
        
        self.frame = ttk.Frame(root)
        self.frame.grid()
        self.frame.config(relief = RIDGE, padding = (50,25))
        

        #title for program
        self.label_title = ttk.Label(self.frame, text = 'Program to Transfer New Files to Destination Folder \nFollow the instructions below:\n 1. Browse and find your source folder \n 2. Browse and find your destination folder \n 3. Press go to execute the file transfer').grid(row=0, columnspan=3)

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

        self.v = StringVar()
        self.lastTransferLabel = ttk.Label(self.frame, textvariable = self.v)
        self.v.set('Last Transfer occured at...' + self.show_last_time()[0])
        self.lastTransferLabel.grid(row = 6, column = 0, columnspan = 3)

###### SQLite Database information

        self.conn = sqlite3.connect('timeoftransfer.db')
        self.c = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.c.execute('CREATE TABLE IF NOT EXISTS transferTimes (epochTime REAL, datestamp TEXT)')
        self.c.execute('SELECT * FROM transferTimes')
        if self.c.fetchall() ==[]:
            self.c.execute("INSERT INTO transferTimes (epochTime, datestamp) VALUES(0.0,'2017-02-23')")
            self.v.set("There is no data to display")
            self.conn.commit()

    def transferTime_go(self):   ####fucntion for database to transfer datestamp of file into the database, and show the year, month, day
        self.conn = sqlite3.connect('timeoftransfer.db')
        self.c = self.conn.cursor()
        self.c.execute("INSERT INTO transferTimes (epochTime, datestamp) VALUES (?,?)", (self.now, str(time.strftime('%Y-%m-%d %H:%M:%S'))))
        self.con.commit()
        self.c.close()
        self.conn.close()

    def show_last_time (self):  ###function to fetch the most recent datetime from the database
        self.conn = sqlite3.connect('timeoftransfer.db')
        self.c = self.conn.cursor()
        self.c.execute('SELECT datestamp FROM transferTimes ORDER BY datestamp DESC')
        last_time = self.c.fetchone()
        self.c.close()
        self.conn.close()
        return (last_time)

        
###Functions for file transfer and dB program
   
    def askSource(self):
         self.source = filedialog.askdirectory()
         return self.source

    def askDestination(self):
        self.destination = filedialog.askdirectory()
        return self.destination


    def file_transfer(self):  ######function to transfer files based on whether it was modifed within las 24hr
        for file in os.listdir(self.source):
            last_date_modified = datetime.fromtimestamp(os.path.getmtime(self.source + '/' + file))
            now = datetime.now()
            time = (now - last_date_modified)
            time_range = timedelta(days=1)
            
            if  time <= time_range:
                
                shutil.copy(self.source + '/' + file,self.destination)
                print(file)

    def go (self):   ###function to display the time that the last file transfer occured
        fromSource = self.entry_source.get()
        toDestination = self.entry_destination.get()
        self.filecopy (fromSource, toDestination)
        self.transferTime_go()
        self.v.set('Last Transfer occured at...' + self.show_last_time()[0])
           

    
if __name__ == "__main__":

    root = Tk()
    app = FileTransfer(root)
    root.title('Gui for_ File Transfer')
    root.resizable(TRUE,TRUE)
    root.mainloop()

 
