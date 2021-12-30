# December 2021, Hackathon, North Park Secondary School
# Number Systems Converter
# By : Mrudul Suresh (735571) , Harsh Patel (678847)

from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from Hackathon import functions as f

root = tk.Tk()
root.title("Number Systems Converter")
data_types = ["Decimal -> Binary", "Binary -> Decimal", "Decimal -> Octal",
              "Octal -> Decimal", "Hexadecimal -> Decimal", "Decimal -> Hexadecimal"]

current = 0

canvas = tk.Canvas(root, width=400, height=600)
canvas.grid(columnspan=3, rowspan=6)

# Grey Banner
selection_banner = Frame(root, width=410, height=80, bg="#c8c8c8")
selection_banner.grid(columnspan=3, rowspan=1, row=1)

# Turquoise Banner
main_content = Frame(root, width=410, height=380, bg="#20bebe")
main_content.grid(columnspan=3, rowspan=3, row=2)

# Output Frame and Output Label
Hlbl = tk.Label(root, text="Conversion Output:", bg="#20bebe", font=("Arial", "18", "bold"))
Hlbl.grid(column=1, row=4, sticky=N)

lblFrame = tk.LabelFrame(root, width=300, height=100, bd=4, bg="#c8c8c8")
lblFrame.grid(column=0, row=4, columnspan=3)

Olbl = tk.Label(root, text="", bg="#c8c8c8")
Olbl.grid(column=0, row=4, columnspan=3)


def execute():
    print("executed")
    inp = inputtxt.get()
    str = f.choose(current + 1, inp)
    print(str)
    Olbl.config(text=str)


def scroll_left():
    global current
    current -= 1
    if current == -1:
        current = 5
    selection_lbl.config(text=data_types[current])


def scroll_right():
    global current
    current += 1
    if current == 6:
        current = 0
    selection_lbl.config(text=data_types[current])


# logo
logo = Image.open('logo1_whitebg.jpg')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(columnspan=3, column=0, row=0)
# Currently Selected Type Label
selection_lbl = tk.Label(root, text=data_types[current], bg="#c8c8c8")
selection_lbl.grid(column=1, row=1)

# instructions
instructions = tk.Label(root, text="Select the Data type you want to convert to and \n then type your number "
                                   "in the text box below:", font="Raleway", bg="#20bebe")
instructions.grid(columnspan=3, column=0, row=2)

# input text field
inputtxt = tk.Entry(root, justify=CENTER, selectborderwidth=3, relief=RIDGE)
inputtxt.grid(columnspan=3, column=0, row=3, sticky=N)

submit_btn = tk.Button(root, text="Submit", command=lambda: execute(), font=("Raleway", 12, "bold"), height=2, width=15)
submit_btn.grid(column=1, row=3)

# Selection buttons
back_button = tk.Button(root, text="<", height=2, width=2, command=lambda: scroll_left())
back_button.grid(column=0, row=1)

forward_button = tk.Button(root, text=">", height=2, width=2, command=lambda: scroll_right())
forward_button.grid(column=2, row=1)

root.mainloop()
