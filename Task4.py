from tkinter import *
from tkinter.font import BOLD
from tkinter.ttk import *


window = Tk()
window.title('Example')
window.geometry('315x140')

style = Style()
style.configure('Bottom.TLabel', background='#a3f8ff', justify='center', font=(BOLD,10))
style.configure('TLabel', background='#FFFFFF', font=(BOLD,10))
style.configure('TFrame', background='#a3f8ff', font=(BOLD,10))
window.configure(background='#FFFFFF')

DogPhoto = PhotoImage(file='dog.png')
Label(window,image=DogPhoto).place(x=86,y=1)
Label(window,text='Pochacco!').place(x=156,y=38)
frame1= Frame(window,width=140)
frame1.place(y=100,x=0)
text = Label(frame1,text='A cuddly litte puppy! This is from the same \ncreators who brought you Keropi and Kero Kero', style='Bottom.TLabel').pack(anchor=CENTER,padx=20,pady=2)


window.mainloop()