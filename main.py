from tkinter import *
import googletrans
from googletrans import Translator

root = Tk()
translator = Translator()


def translatingTODO(newitem):
    translated_item = translator.translate(newitem, dest='fr', src='en').text
    print(translated_item)
    # add to dictionary with the translated version


word = StringVar()
todothing = Entry(root, textvariable=word)
todothing.pack()
translatingTODO(word)

root.mainloop()
