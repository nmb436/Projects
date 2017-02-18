import shutil
import os

source = 'C:/Users/Student/Desktop/source/'  
destination = 'C:/Users/Student/Desktop/destination'

def start():

    for files in os.listdir(source):
        if files.endswith(".txt"):
            shutil.move(source + files,destination)

if __name__ == '__main__':
    start()
    

   

        

