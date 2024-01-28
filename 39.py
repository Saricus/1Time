#Pierwszy program gui
from tkinter import *


def wyswietl():
    print('Hej hooo')



window = Tk() #nazwa
window.geometry('400x100') #rozmiar okna
frame = Frame() #okno
frame.pack(expand=True)
Label( 
    master=frame,
    text='Witaj w appce',
    font=18
).pack(side=TOP)
Button(
    master=frame,
    text='Nacisnij mnie',
    command=wyswietl,
    font=18
).pack(side=BOTTOM)
window.mainloop()