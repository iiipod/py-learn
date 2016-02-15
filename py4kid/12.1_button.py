from Tkinter import *

def hello():
    print('Hello there')

tk = Tk()

tk.title('Hello Tkinter')
tk.geometry('200x100')

btn = Button(tk, text="click me", command = hello)
btn.pack()

mainloop()

