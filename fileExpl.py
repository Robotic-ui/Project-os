from tkinter import *
from tkinter import filedialog 
import os 

def openFile():
    filepath = filedialog.askopenfilename(initaldir='/', title="Open Files", filetype=("text files",))
    os.startfile(filepath)

window = Tk()
button = Button(text="open", command=openFile)

button.pack()
window.mainloop()
