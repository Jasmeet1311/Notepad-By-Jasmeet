#                                                  Notepad
from tkinter import *
import tkinter.messagebox as tmsg
import tkinter.filedialog as tf
import os
def newFile():
    global file
    root.title("Untitled- Notepad")
    file= None
    text.delete(1.0,END)

def openFile():
    global file
    file=tf.askopenfilename(defaultextension=".txt",filetypes=[("All files","*.*"),("Text documents","*.txt")])
    if file=="":
        file= None
    else:
        root.title(os.path.basename(file)+" - Notepad")
        text.delete(1.0,END)
        f = open(file,"r")
        text.insert(1.0,f.read())
        f.close()



def saveFile():
    global file
    if file == None:
        file=tf.asksaveasfilename(initialfile="Untitled.txt",defaultextension=".txt",filetypes=[("All files","*.*"),("Text documents","*.txt")])
        if file =="":
            file = None
        else:
            #Save as a new file
            f=open(file,"a")
            f.write(text.get(1.0,END))
            f.close()
            root.title(os.path.basename(file)+" - Notepad")
    else:
        # Save the file
        f=open(file, "a")
        f.write(text.get(1.0, END))
        f.close()
def cut():
    text.event_generate(("<<Cut>>"))
def copy():
    text.event_generate(("<<Copy>>"))
def paste():
    text.event_generate(("<<Paste>>"))
def about():
    about="Notepad is a simple text Editor that is created by Jasmeet.\nIt creates and edits simple plain documents"
    tmsg.showinfo("Notepad",about)
def close():
    root.destroy()
if __name__ == '__main__':
    root = Tk()
    root.geometry('500x400')
    root.title("Untitled-Notepad")
    root.wm_iconbitmap("notepad-2.ico")
    # Scrollbar
    scrollbar = Scrollbar(root)

    scrollbar.pack(side=RIGHT, fill=Y)

    # text area
    text =Text(root,font="cosmicsansms 14",yscrollcommand=scrollbar.set)
    text.pack(expand= True,fill=BOTH)
    scrollbar.config(command=text.yview)
    # This variable will point to that file that we have opened
    file= None

    # Menubar
    mainmenu= Menu(root)
    filemenu = Menu(mainmenu,tearoff=0)
    # To open new file
    filemenu.add_command(label="New",command=newFile)
    # To open a new file
    filemenu.add_command(label="Open",command= openFile)
    # To save a new file
    filemenu.add_command(label="Save",command=saveFile)
    filemenu.add_separator()
    filemenu.add_command(label="Exit",command =close)
    mainmenu.add_cascade(label="File",menu=filemenu)


    # Edit Menu
    editmenu= Menu(mainmenu,tearoff=0)
    # To cut the content
    editmenu.add_command(label="Cut",command=cut)
    # To copy the content
    editmenu.add_command(label="Copy",command= copy)
    # To Paste the copied content
    editmenu.add_command(label="Paste",command= paste)
    mainmenu.add_cascade(label="Edit",menu=editmenu)

    # Help menu
    helpmenu= Menu(mainmenu,tearoff=0)
    helpmenu.add_command(label="About Notepad",command= about)
    mainmenu.add_cascade(label="Help",menu=helpmenu)
    root.config(menu=mainmenu)


    root.mainloop()