# Python Ver: 3.11
#
# Author: Noah Ketcham
#
# Purpose:  Creating an app to track information about students.
#
# Tested OS: This code was written and tested to worl with Windows 10.

from tkinter import *
import tkinter as tk

#accessing other modules
import student_func
import student_gui

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        #Frame configuration
        self.master = master
        self.master.minsize(500,500)  #(H/W)
        self.master.maxsize(500,500)

        student_func.center_window(self,500,500) #Centers app onscreen
        self.master.title("Student Tracking")
        self.master.configure(bg= "#F0F0F0")

        self.master.protocol("WM_DELETE_WINDOW", lambda: student_func.ask_quit(self))
        arg = self.master

        student_gui.load_gui(self) #loads widgets from student_gui

        #menu
        menubar = Menu(self.master)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", underline=1,accelerator="Ctrl+Q",command=lambda: student_func.ask_quit(self))
        menubar.add_cascade(label="File", underline=0, menu=filemenu)
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_separator()
        helpmenu.add_command(label="How to use this program")
        helpmenu.add_separator()
        helpmenu.add_command(label="About This Phonebook Demo") # add_command is a child menubar item of the add_cascde parent item
        menubar.add_cascade(label="Help", menu=helpmenu) # add_cascade is a parent menubar item (visible heading)
       
        self.master.config(menu=menubar, borderwidth='1')


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()

