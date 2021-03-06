from Tkinter import *
import random
import time

class Game:
    def __init__(self):
        self.tk = Tk()
        self.tk.title("Mr. Stick Man Races for the Exit")
        self.tk.resizable(0, 0)
        self.tk.wm_attributes("-topmost", 1)
        self.canvas = Canvas(self.tk, width=500, height=500, highlightthickness=0)
        self.canvas.pack()
        self.tk.update()
        self.canvas_height = 500
        self.canvas_width = 500
        self.bg = PhotoImage(file="15_image/background.gif")
        w = self.bg.height()
        h = self.bg.width()
        for x in range(0, 5):
            for y in range(0, 5):
                self.canvas.create_image(x * w, y * h, image=self.bg, anchor='nw')
        self.sprites = []
        self.running = True

    def mainloop(self):
        while 1:
            if self.running == True:
                for self.sprite in  self.sprites:
                    sprite.move()
            self.tk.update_idletasks()
            self.tk.update()
            time.sleep(0.01)
class Coords:
    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

def within_x(co1, co2):
#        if co1.x1 > co2.x1 and co1.x1 < co2.x2:
#            return True
#        elif co1.x2 > co2.x1 and co1.x2 < co2.x2:
#            return True
#        elif co2.x1 > co1.x1 and co2.x1 < co1.x2:
#            return True
#        elif co2.x2 > co1.x1 and co2.x2 < co1.x1:
#            return True
#        else:
#            return False

    if (co1.x1 > co2.x1 and co1.x1 < co2.x2) or (co1.x2 > co2.x1 and co1.x2 < co2.x2) or (co2.x1 > co1.x1 and co2.x1 < co1.x2) or (co2.x2 > co1.x1 and co2.x2 < co1.x2):
        return True
    else:
        return False

### Test ###
c1 = Coords(40, 40, 100, 100)
c2 = Coords(50, 50, 150, 150)
print within_x(c1, c2)

g = Game()
g.mainloop()
