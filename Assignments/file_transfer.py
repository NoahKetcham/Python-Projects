import tkinter as tk
from tkinter import *
import tkinter.filedialog
import os
import shutil
from datetime import datetime, timedelta


class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)
        # sets title og GUI window
        self.master.title("File Transfer")

        #Creates button to select files from source directory
        self.sourceDir_btn = Button(text='Select Source', width=20, command=self.sourceDir)
        #Positions source button in gui using tkinter grid()
        self.sourceDir_btn.grid(row=0, column=0, padx=(20, 10), pady=(30, 0))

        #creates entry for source directory selection
        self.source_dir = Entry(width=75)
        #Positions entry in GUI using tkinter grid() padx and pady are the same as the button to ensure they will line up
        self.source_dir.grid(row=0, column=1, columnspan=2, padx=(20, 10), pady=(30, 0))

        self.destDir_btn = Button(text="Select Destination", width=20, command=self.destDir)
        #positions destination button in GUI using tkinter grid() on the next row under the source button
        self.destDir_btn.grid(row=1, column=0, padx=(20, 10), pady=(15,10))

        #Creates entry fpr destination directory selection
        self.destination_dir = Entry(width=75)
        #Positions entry inGUI using tkinter grid() padx and pady are the same as the button to ensure they will line up
        self.destination_dir.grid(row=1, column=1, columnspan=2, padx=(20, 10), pady=(15, 10))

        #Creates button to transfer files
        self.transfer_btn = Button(text='Transfter Files', width=20, command=self.transferFiles)
        #Positions transfer files button
        self.transfer_btn.grid(row=2, column=1, padx=(200, 0), pady=(0, 15))

        #Creates an exit button
        self.exit_btn = Button(text='Exit', width=20, command=self.exit_program)
        #Positions the exit button
        self.exit_btn.grid(row=2, column=2, padx=(10, 40), pady=(0, 15))

    
    #Creates function to select source directory.
    def sourceDir(self):
        selectSourceDir = tkinter.filedialog.askdirectory()
        #The .delete(0, END) will clear the content that is inserted in the entry widget, this allows the path to be inserted into the entry widget properly.
        self.source_dir.delete(0, END)
        #The .insert method will insert the user selection to the source_dir Entry
        self.source_dir.insert(0, selectSourceDir) 


    #Creates function to select source directory.
    def destDir(self):
        selectDestDir= tkinter.filedialog.askdirectory()
        #The .delete(0, END) will clear the content that is inserted in the entry widget, this allows the path to be inserted into the entry widget properly.
        self.destination_dir.delete(0, END)
        #The .insert method will insert the user selection to the source_dir Entry
        self.destination_dir.insert(0, selectDestDir) 


    #Creates function to transfer files from one directory to another
    def transferFiles(self):
        #Gets the current time
        now = datetime.now()
        #Utilizing timedelta
        oneDay = now - timedelta(hours=24)
        
        #Gets source directory
        source = self.source_dir.get()
        #gets destination directory
        destination = self.destination_dir.get()
        #Gets a list of files in the source directory
        source_files = os.listdir(source)
        
        #Runs through each file in the source directory
        for file in source_files:
            #Getsa the full file path
            file_path = os.path.join(source, file)
            #gets the most recent modification time of a file
            file_mod_time = datetime.fromtimestamp(os.path.getmtime(file_path))

            #Cheacks if the file was modified in the last 24 hours
            if file_mod_time > oneDay:
                #Moves file to destinastion folder
                shutil.move(file_path, destination)
                print(file + "was transferred succesfully")

    
    #Creates function to exit program
    def exit_program(self):
        #root is the main GUI window, the tkinter destroy method tellls python to terminate root.mainloop and all widgets inside the gui window.
        root.destroy()
    

    

if __name__ == '__main__':
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()



