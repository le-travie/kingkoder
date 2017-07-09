#############################
# Program Name: KingKoder
# Author: Jaime ( pronounced Jay-Me ) T. Kingston
# Version: 1.1 - Added my own icon :-))
# Date Created: 2010-11-25
# Usage: KingKoder is used to encode and decode files,
#       programs, etc.. using python's uu module. After encoding
#       a file with the extension ".kkd" file will be created, it is recommmended that you
#       name them appropriatly for example mythings.zip should be renamed
#       to mythings.zip.kkd, so it won't be confused with other encoded
#       files.
# History: Version 0.5 - No Gui, could only encode files in the current working
#                       directory
#           Version 1.0 - Gui added, added encode and decode buttons
#
#           Version 1.1 - file browser button added, put in my own personal
#                           icon and set maximun and minimun window size.
#############################

import tkMessageBox, tkFileDialog
import uu, os
from Tkinter import*



class KingKoder(Frame):
    def __init__ (self, parent=0):
        Frame.__init__ (self,parent)
        self.master.title('KingKoder')
        #self.master.iconbitmap('kkico.ico')
        self.kkUI()

# Change current directory to C:

        os.chdir('C:/')

# Start of GUI code

    def kkUI (self):

        eFile = Frame(self)
        Label(eFile, text = "Filename: ").pack(side = "left")
        self.fName = Entry (eFile)
        self.fName.pack(side = LEFT, padx = 5)
        self.fbBut = Button(eFile, text = "Browse",
                            command=self.fiBr)
        self.fbBut.pack(side = LEFT, anchor = W, padx = 5)


# Encode and Decode button codes

        eNdE = Frame(eFile, borderwidth = 1, relief=RAISED)

        self.ecBut = Button (eFile, text = "Encode",
                         command = self.encode)
        self.ecBut.pack(side = BOTTOM, anchor=W)

        self.dcBut = Button (eFile, text = "Decode",
                         command = self.decode)
        self.dcBut.pack(side = BOTTOM, anchor = W)

        eFile.pack(side = TOP, fill = BOTH)
        eNdE.pack(side=BOTTOM,anchor=W)
        self.pack()


# Button Function Code

# Browse Button

    def fiBr(self):
        self.fName.delete(0,END) # erase entry box
        sFile = tkFileDialog.askopenfilename() # Search for a file to encode
        wFile = os.path.basename(sFile) # splits the file name from the directory name and assigns it to a variable
        nWp = os.path.dirname(sFile) # splits the directory name from file name and assign it to a variable
        os.chdir(nWp) # changes the current directory to that of the file
        self.fName.insert(END, wFile) # inserts the file name into the entry box


# Encode button code

    def encode(self):
        self.name = self.fName.get() # gets the file name from the entry box
        if os.path.exists(self.name): # Checks to see wheather the file exists in the current directory, if true its is encoded if false an error message is displayed
            uu.encode(self.name, self.name+'.kkd', mode = None, name = None)
            tkMessageBox.showinfo("Encoding...", " Encoding of file successful!")
        else:
            tkMessageBox.showerror("Critical Error", " File Name is Invalid!")

# Decode Button Code

    def decode(self):
        self.name = self.fName.get()
        if os.path.exists(self.name):
            uu.decode(self.name, mode = None, quiet = 0)
            tkMessageBox.showinfo("Decoding... ", "Decoding of File Successful!")
        else:
            tkMessageBox.showerror("Critical Error", " File name is Invalid, Connot decode")

myApp = KingKoder()
myApp.master.maxsize(285, 50) # sets the maximum window size
myApp.master.minsize(285, 50) # sets the minimum window size
myApp.mainloop()
