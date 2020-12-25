import random
from tkinter import *
window = Tk()
window.title('my app')
window.geometry("400x300")
def phrase_generator():
    phrases = ["Hllo","What's up","Aloha","Hallo","привет"]
    name = entry1.get()
label1 = Label (text = 'Welcome to my app',font = ('Times To Roman',20))
label1.place(y = 0,x = 70)
label2 = Label (text = 'What is your name')
label2.place(y = 33,x = 70)
button1 = Button (text = 'click me',bg = 'red')
button1.place(y = 48,x = 100)
text1 = Text(height=10,width=25)
text1.place(y = 68,x = 0)
entry1 = Entry(width=15)
entry1.place(y = 33,x = 225)
window.mainloop()
