from tkinter import*
from time import strftime
import sys

window=Tk()
window.title("Digital Clock")
window.geometry("500x500")
window.configure(bg="black")

def clock():
    clock_structure=strftime("%H:%M:%S %p    %d:%y")
    l.config(text=clock_structure)
    l.after(1000,clock)

l=Label(window,fg="white",bg="black",font=("Times New Roman",20))
l.pack(anchor=CENTER)
fun_call=clock()

window.mainloop()
