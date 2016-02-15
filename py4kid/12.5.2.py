from Tkinter import *
import random

tk = Tk()
tk.title("Tkinter random rectangle")
canvas = Canvas(tk, width=400, height=400)
canvas.pack()

def random_rectangle(width, height, fill_color):
    x1 = random.randrange(width/2)
    y1 = random.randrange(height/2)
    x2 = x1 + random.randrange(width/2)
    y2 = y1 + random.randrange(height/2)
    canvas.create_rectangle(x1, y1, x2, y2, fill=fill_color)

#for x in range(0, 100):
#    random_rectangle(400, 400, 'green')
random_rectangle(400, 400, 'green')
random_rectangle(400, 400, 'red')
random_rectangle(400, 400, 'blue')
random_rectangle(400, 400, '#ffd800')
random_rectangle(400, 400, '#35ff35')

mainloop()
