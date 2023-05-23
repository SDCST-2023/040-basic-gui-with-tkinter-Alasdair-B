from tkinter import *
from tkinter.font import BOLD
from tkinter.ttk import *


window = Tk()
window.title('Example')

style = Style()
style.configure('TEnter', borderwidth = '3', relief=GROOVE)
style.configure('Bottom.TLabel', background='#20f8fc', font=(BOLD,10))
style.configure('TLabel', background='#FFFFFF', font=(BOLD,10))
style.configure('TButton', borderwidth = 0, relief=GROOVE, font=(BOLD,10))
window.configure(background='#FFFFFF')

DogPhoto = PhotoImage(file='dog.png')
Label(window,image=DogPhoto).grid(column=2,row=1)
Label(window,text='Pochacco!')
text = Label(window,text='A cuddly litte puppy! This is from the same \ncreators who brought you Keropi and Kero Kero', style='Bottom.TLabel').grid(column=1,row=2,columnspan=4,ipadx=4,ipady=5)


window.mainloop()