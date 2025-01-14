#!/usr/bin/env python
from tkinter import *
from tkinter.filedialog import *
from tkinter import messagebox
import tkinter.font
import os
import platform 


w = Tk()
w.title("Haardcode")
w.geometry("800x600")
scroll_bar=Scrollbar(w)


def save_as_file():
    save_as_file.name = None
    f=asksaveasfile(mode="w", defaultextension=".txt")
    if f is None:
        return 
    else:
        save_as_file.name = f.name
        base = os.path.basename(save_as_file.name)
        w.title("Haardcode - {}".format(base))
    text2save=str(main_text.get(1.0, END))
    f.write(text2save)
    f.close()
def open_file():
    open_file.filename = askopenfile(mode = "r")
    if open_file.filename is not None:
        content = open_file.filename.read()
        main_text.delete(0.0, END)
        main_text.insert(END, content) 
def save():
    try:
        if save_as_file.name is not None:
            with open (save_as_file.name, 'r+') as myfile:
                data = myfile.read()
                myfile.seek(0)
                myfile.write(str(main_text.get(1.0, END)))
                myfile.truncate()
        elif save_as_file.name is None and open_file.filename is not None:
            with open (open_file.filename, 'r+') as myfile:
                data = myfile.read()
                myfile.seek(0)
                myfile.write(str(main_text.get(1.0, END)))
                myfile.truncate()
    except AttributeError:
        save_as_file()

def exit():
    w.destroy()

def run_file():
    operating_system = platform.system()
    if operating_system == 'Linux':
        try:
            if save_as_file.name is not None:
                os.system("python {}".format(save_as_file.name))
        except AttributeError:
            if open_file.filename is not None:
                os.system("python {}".format(open_file.filename.name))
    elif operating_system == 'Windows':
        try:
            if save_as_file.name is not None:
                os.system("python {}".format(save_as_file.name))
        except AttributeError:
            if open_file.filename is not None:
                os.system("python {}".format(open_file.filename.name))


def new():
    main_text.delete(0.0, END)
    w.title("Haardcode")

#Shitty code 
"""
def preferences():
    os.system("python preferences.py")
"""
def about():
    os.system("python about.py")

#printing
def print_file(): 
    a = Tk()
    a.title("Print")
    a.configure(bg="#282828")
    a.resizable(width=False, height=False)
    font=("Cascadia Code", 14)
    operating_system = platform.system()
    def normal_print():
        #lpr file.text
        if operating_system == 'Linux':
            try:
                if save_as_file.name is not None:
                    os.system("lp {}".format(save_as_file.name))
                    a.destroy()
            except AttributeError:
                if open_file.filename is not None:
                    os.system("lp {}".format(open_file.filename.name))
                    a.destroy()
       
        elif operating_system == 'Windows':
            try:
                if save_as_file.name is not None:
                    os.system("notepad /p {}".format(save_as_file.name))

            except AttributeError:
                if open_file.filename is not None:
                    os.system("notepad /p {}".format(open_file.filename.name))
    #Before printing set default printer
    heading = Label(a, text="Printing options", font=font, fg="white", bg="#282828")
    note = Label(a, text="Note: Before you print, please set your default printer", font=font, fg="white", bg="#282828")
    #normal button
    normal = Button(a, text="Normal Print", font=font, command=normal_print)
    #positions
    heading.grid(row=0, column=0, padx=10, pady=10)
    note.grid(row=1, column=0, padx=10, pady=10)
    normal.grid(row=2, column=0, padx=10, pady=10)
    a.mainloop()

#Font
font = tkinter.font.Font(family='Cascadia Code', size=14)

#Menubar
menubar=Menu(w, font=font, bg="#282828", fg="#f8f8f2", relief=FLAT)

#Files tab
files = Menu(menubar, tearoff=0, font=font, bg="#282828", fg="#f8f8f2", relief=FLAT)
files.add_command(label="New", command=new)
files.add_command(label="Open", command=open_file)
files.add_command(label="Save", command=save)
files.add_command(label="Save as..", command=lambda:save_as_file())
files.add_command(label="Print", command=print_file)
files.add_command(label="RUN", command=run_file)
files.add_separator()
files.add_command(label="Exit", command=exit)
menubar.add_cascade(label="File", menu=files)

#Edit
edit = Menu(menubar, tearoff=0, font=font, bg="#282828", fg="#f8f8f2", relief=FLAT)
#edit.add_command(label="Preferences", command=preferences)
#menubar.add_cascade(label="Edit", menu=edit)

#About
menubar.add_command(label="About", command=about)

#Help 
menubar.add_command(label="Help")

#Main Text Box
main_text = Text(w, width=800, height=600, wrap=WORD, font=font, bg="#282828", fg="#f8f8f2", insertbackground='white', highlightthickness=0, relief=SOLID)

#positions
main_text.grid(row=1, column=0)
w.config(menu=menubar)
w.mainloop()
