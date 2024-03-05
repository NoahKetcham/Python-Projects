Python 3.11.7 (tags/v3.11.7:fa7a6f2, Dec  4 2023, 19:24:49) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from tkinter import *
>>> win = Tk()
>>> b1 = Button(win, text='One')
>>> b2 = Button(win, text = 'Two')
>>> 
>>> b1.pack()
>>> b2.pack()
>>> 
>>> b1.pack(side=LEFT)
>>> b2.pack(side =LEFT)
>>> 
>>> b1.pack(side=LEFT, padx = 10)
>>> b2.pack(side =LEFT, padx = 10)
