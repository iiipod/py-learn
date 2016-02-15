from Tkinter import *

tk = Tk()
tk.title("Tkinter load image")
canvas = Canvas(tk, width=400, height=400)
canvas.pack()
my_image=PhotoImage(file='/home/pl/photo/01.gif')
canvas.create_image(0, 0, anchor=NW, image=my_image)

mainloop()
