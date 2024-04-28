from time import sleep
import tkinter
from tkinter import *

def NewFile():
    texto_area.delete(1.0, "end")

def Save():
   container = texto_area.get(1.0, "end")
   file = open("notepad.txt", "w")
   file.write(container)
   file.close()
 
def Open():
    file = open("notepad.txt", "r")   
    container = file.read()
    texto_area.insert(1.0, container)

def UpdateFont():
    size = spin_size.get()
    font = spin_font.get()
    texto_area.config(font="{} {}".format(font, size))
    
app = Tk()
app.title("Notepad")
app.geometry("1280x720")
app.minsize(width=1280, height=720)

frame = tkinter.Frame(app, height=30)
frame.pack(fill="x")

font_text = tkinter.Label(frame, text="  font: ")
font_text.pack(side="left")

spin_font = tkinter.Spinbox(frame, values=("Arial", "Verdana"))
spin_font.pack(side="left")

font_size = tkinter.Label(frame, text=" Font size: ")
font_size.pack(side="left")

spin_size = tkinter.Spinbox(frame, from_=0, to=60)
spin_size.pack(side="left")

button_update = tkinter.Button(frame, text="UP", command=UpdateFont)
button_update.pack(side="left")

texto_area = tkinter.Text(app, font="Arial 20 bold", width=1280, height=720)
texto_area.pack()

main_menu = tkinter.Menu(app)

file_menu = tkinter.Menu(main_menu, tearoff=0)
file_menu.add_command(label="New", command=NewFile)
file_menu.add_command(label="Save", command=Save)
file_menu.add_command(label="open", command=Open)
file_menu.add_command(label="Exit", command=app.quit)

main_menu.add_cascade(label="File", menu=file_menu)
app.config(menu=main_menu)

app.mainloop()
