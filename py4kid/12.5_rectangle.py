from Tkinter import *

tk = Tk()
canvas = Canvas(tk, width=400, height=400)
tk.title("Tkinter rectangle")
canvas.pack()
canvas.create_rectangle(10, 10, 50, 50)
canvas.create_rectangle(50, 50, 300, 100)
canvas.create_rectangle(10, 100, 50, 300)

mainloop()
