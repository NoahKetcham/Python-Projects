Python 3.11.7 (tags/v3.11.7:fa7a6f2, Dec  4 2023, 19:24:49) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from tkinter import *
>>> win = Tk()
>>> v = StringVar()
>>> e = Entry(win, textvariable = v)
>>> e.pack()
>>> 
>>> v.get()
'This is a test'
>>> 
>>> v.set("This is set by the program")
