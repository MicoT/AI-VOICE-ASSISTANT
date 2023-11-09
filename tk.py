from tkinter import *
from search import info


win = Tk()
win.geometry('320x50');win.title('AI VOICE ASSISTANT')
button = Button(win, text="Speak", command = info )
button.pack()
win.mainloop()
