from tkinter import *
from tkinter import Checkbutton

import googletrans
from googletrans import Translator

translator = Translator()
root = Tk()
to_do = {}

def exitAdding(entrybox,first, second):
    entrybox.destroy()
    first.destroy()
    second.destroy()

def completed(event, check):
    check.destroy()

def translating(thing):
    translated = translator.translate(text=thing, dest='fr', src='en').text
    return translated


def adding(word):
    english = word.get()
    french = translating(english)
    to_do[english] = french
    check: Checkbutton = Checkbutton(root, text=french)
    check.pack()

def buttonPressed():
    word = StringVar
    newitem = Entry(root, textvariable = word)
    newitem.pack()
    button_2 = Button(root, text = "Add to list?",command = lambda :adding(newitem))
    button_2.pack()
    button_3 = Button(root, text = "Stop Adding?", command = lambda: exitAdding(newitem, button_2,button_3))
    button_3.pack()



button_1 = Button(root, text="New To Do",command = buttonPressed)
button_1.pack()










root.mainloop()
