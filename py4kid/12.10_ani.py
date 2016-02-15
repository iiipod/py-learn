import time
from Tkinter import *

tk = Tk()
tk.title("Tkinter move")
ani = Canvas(tk, width=400, height=400)
ani.pack()
ani.create_polygon(10, 10, 10, 60, 50, 35)
for x in range(0, 60):
    ani.move(1, 5, 5)
    tk.update()
    time.sleep(0.05)

for x in range(0, 60):
    ani.move(1, -5, -5)
    tk.update()
    time.sleep(0.05)

mainloop()
