from tkinter import *
from tkinter.font import BOLD
from tkinter.ttk import *


window = Tk()
window.title('T-Town Veterinary Clinic Database')

style = Style()
style.configure('TEnter', borderwidth = '3', relief=GROOVE)
style.configure('TLabel', background='#FFFFFF', font=(BOLD,10))
style.configure('TButton', borderwidth = 0, relief=GROOVE, font=(BOLD,10))
window.configure(background='#FFFFFF')

DogPhoto = PhotoImage(file='dog.png')
Label(window,image=DogPhoto).grid(column=1,row=1,rowspan=3)
Button(window,text='Search by Name').grid(column=4,row=1, sticky='e')
Entry(window).grid(column=5,row=1,sticky='w',ipadx=15,padx=7,ipady=2.5)
Label(window, text='Client Database').grid(column=3, row=2)
Label(window, text='Name').grid(column=1, row=4)
Label(window, text='Type').grid(column=2, row=4)
Label(window, text='Breed').grid(column=3, row=4)
Label(window, text='Owner').grid(column=4, row=4)
Label(window, text='Birthdate').grid(column=5, row=4)
Entry(window).grid(column=1,row=5,padx=3,ipady=2.5)
Entry(window).grid(column=2,row=5,padx=3,ipady=2.5)
Entry(window).grid(column=3,row=5,padx=3,ipady=2.5)
Entry(window).grid(column=4,row=5,padx=3,ipady=2.5)
Entry(window).grid(column=5,row=5,padx=3,ipady=2.5)
Button(window,text='< Previous').grid(column=1,row=6,sticky='w',padx=3,pady=3)
Button(window,text='Save Entry').grid(column=3,row=6,padx=3,pady=3,ipady=4.5)
Button(window,text='Next >').grid(column=5,row=6,sticky='e',padx=3,pady=3)

window.mainloop()