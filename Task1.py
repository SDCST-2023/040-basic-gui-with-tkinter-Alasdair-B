#!python3
from tkinter import *
from tkinter.font import BOLD
from tkinter.ttk import *


window = Tk()
window.title('tk')

style = Style()
style.configure('TEnter', borderwidth = '3', relief=GROOVE)
style.configure('TLabel', font=(BOLD,10))
style.configure('TButton', borderwidth = '3', relief=GROOVE, font=BOLD, width=2)
style.configure('OutBox', borderwidth = '3')

Answer=''
Num1=StringVar
Num2=StringVar

enter1 = Entry(window).grid(column=1,row=1,padx=5,pady=5)
Label(window, text='X').grid(column=2,row=1,pady=5)
enter2 = Entry(window).grid(column=3,row=1,padx=5,pady=5)
Button(window, text='=').grid(column=4,row=1,pady=5)
Out1 = Label(window,textvar=Answer,style='OutBox')
Out1.grid(column=5,row=1,padx=5,pady=5)


window.mainloop()