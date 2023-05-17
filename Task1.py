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
style.configure('OutBox.TLabel', borderwidth = '3', width=10,background='#FFFFFF',font='#000000')

Answer= StringVar(window,'')
Num1= StringVar(window)
Num2= StringVar(window)

def Calculate():
    global Answer
    global Num1
    global Num2
    try:
        a=float(Num1.get())
    except:
        a=0
    try:
        b=float(Num2.get())
    except:
        b=0
    x = str(float(a)*float(b))
    Answer.set(x)
    

enter1 = Entry(window,textvariable=Num1).grid(column=1,row=1,padx=5,pady=5)
Label(window, text='X').grid(column=2,row=1,pady=5)
enter2 = Entry(window,textvariable=Num2).grid(column=3,row=1,padx=5,pady=5)
Button(window, text='=',command=Calculate).grid(column=4,row=1,pady=5)
Out1 = Label(window,textvariable=Answer,style='OutBox.TLabel').grid(column=5,row=1,padx=5,pady=5)


window.mainloop()