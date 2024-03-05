# Python Ver: 3.11
#
# Author: Noah Ketcham (By Daniel A. Christie)
#
# Purpose:  Phonebook demo.  Demonstrating OOP, TKinter GUI Module,
#           using TKinter Parent and Child relationships.
#
# Tested OS: This code was written and tested to worl with Windows 10.

from tkinter import *
import tkinter as tk


# be sure to import our other modules
# so we can have access to them
import phonebook_gui
import phonebook_func


# Frame is the tkinter frame class that our own class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        #define our master frame configuration
        self.master = master
        self.master.minsize(500,300) #(height,width)
        self.master.maxsize(500,300)
        # This CenterWindow method will center our app on the users screen
        phonebook_func.center_window(self,500,300)
        self.master.title("The TKinter Phonebook Demo")
        self.master.configure(bg="#F0F0F0")
        # This protocol method is a tkinter built-in mewthod to catch if
        # the user clicks the upper corne, X on windows os.
        self.master.protocol("WM_DELETE_WINDOW", lambda: phonebook_func.ask_quit(self))
        arg = self.master

        # load in the gui widgets from a separatemodule
        # keeping your code compartmentalized and clutter free
        phonebook_gui.load_gui(self)

        # Instantiate the Tkinter menu dropdown object
        # This is the menu that will appear at the top of our window
        menubar = Menu(self.master)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", underline=1,accelerator="Ctrl+Q",command=lambda: phonebook_func.ask_quit(self))
        menubar.add_cascade(label="File", underline=0, menu=filemenu)
        helpmenu = Menu(menubar, tearoff=0) # defines the particular drop down colum and tearoff=0 means do not separate from menubar
        helpmenu.add_separator()
        helpmenu.add_command(label="How to use this program")
        helpmenu.add_separator()
        helpmenu.add_command(label="About This Phonebook Demo") # add_command is a child menubar item of the add_cascde parent item
        menubar.add_cascade(label="Help", menu=helpmenu) # add_cascade is a parent menubar item (visible heading)
        """
            Finally, we apply the config method of the widget to display the menu
            From here we could also pass in additional aprams for additional 
            functionalityor appearances such as a borderwidth.
        """
        self.master.config(menu=menubar, borderwidth='1')







if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
    
