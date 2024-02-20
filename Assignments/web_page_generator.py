import tkinter as tk 
from tkinter import *
import webbrowser


class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")
        

#-----------------------------BUTTONS/GUI----------------------------------------------------
        """
        self.btn = Button(self.master, text="Defaul HTML Page", width=30, height=2, command=self.defaultHTML)
        self.btn.grid(padx=(10,10), pady=(10,10))
        """

        #Creates the input box for custom text
        self.textLabel = Label(self.master, text="Enter Custom Text or click the default html page button.")
        self.textLabel.grid(row =0, padx=(10, 10), pady=(10, 0))

        self.textEntry = Entry(self.master, width=100)
        self.textEntry.grid(row=1, column=0, padx=(10, 10), pady=(0, 10))

        #Creates the button for the HTML page
        self.btnHTML = Button(self.master, text="Default HTML Page", width=20, height=2, command=self.defaultHTML)
        self.btnHTML.grid(row=2, column=0, padx=(5, 5), pady=(5, 5))
        
        #Creates the submit button
        self.btnSubmit = Button(self.master, text="Submit Custom text", width=20, height=2, command=self.submitHTML)
        self.btnSubmit.grid(row=2, column=1, padx=(5, 5), pady=(5, 5))


#-----------------------------/BUTTONS/GUI----------------------------------------------------
        
#-----------------------------FUNCTIONS----------------------------------------------------

    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        self.createHTML(htmlText)

    def submitHTML(self):
        htmlText = self.textEntry.get()
        if not htmlText: #Uses default text
            htmlText = "Stay tuned for our amazing summer sale!"
        self.createHTML(htmlText)
    
    def createHTML(self, text):
        htmlContent = f"<html>\n<body>\n<h1>{text}</h1>\n</body>\n</html>"
        with open("index.html", "w") as htmlFile:
            htmlFile.write(htmlContent)
        webbrowser.open_new_tab("index.html")

#-----------------------------/FUNCTIONS----------------------------------------------------


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()