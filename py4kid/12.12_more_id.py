# my_triangle
# itemconfig()
from Tkinter import *

tk = Tk()
tk.title('Tkinter event')
ani = Canvas(tk, width=400, height=400)
ani.pack()
my_triangle = ani.create_polygon(10, 10, 10, 60, 50, 35)
ani.itemconfig(my_triangle, fill='blue', outline="red")

### 1 ###
#def movetriangle(event):
#    ani.move(1, 5, 0)
#ani.bind_all('<KeyPress-Return>', movetriangle)

def movetriangle(event):
    if event.keysym == 'Up':
        ani.move(my_triangle, 0, -3)
    elif event.keysym == 'Down':
        ani.move(my_triangle, 0, 3)
    elif event.keysym == 'Left':
        ani.move(my_triangle, -3, 0)
    else:
        ani.move(my_triangle, 3, 0)

ani.bind_all('<KeyPress-Up>',movetriangle)
ani.bind_all('<KeyPress-Down>', movetriangle)
ani.bind_all('<KeyPress-Left>', movetriangle)
ani.bind_all('<KeyPress-Right>', movetriangle)


mainloop()
