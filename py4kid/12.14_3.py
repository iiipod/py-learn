from Tkinter import *

tk = Tk()
tk.title("Tkinter load image")
ani = Canvas(tk, width=400, height=400)
ani.pack()
my_image=PhotoImage(file='/home/pl/photo/01.gif')
my_pic = ani.create_image(0, 0, anchor=NW, image=my_image)


def movetriangle(event):
    if event.keysym == 'Up':
        ani.move(my_pic, 0, -3)
    elif event.keysym == 'Down':
        ani.move(my_pic, 0, 3)
    elif event.keysym == 'Left':
        ani.move(my_pic, -3, 0)
    else:
        ani.move(my_pic, 3, 0)

ani.bind_all('<KeyPress-Up>',movetriangle)
ani.bind_all('<KeyPress-Down>', movetriangle)
ani.bind_all('<KeyPress-Left>', movetriangle)
ani.bind_all('<KeyPress-Right>', movetriangle)


mainloop()
