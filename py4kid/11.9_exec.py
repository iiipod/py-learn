import turtle

t = turtle.Pen()

def eight(size,filled):
    if filled == True:
        t.begin_fill()
    for x in range(1, 9):
        t.forward(size)
        t.right(45)
    if filled == True:
        t.end_fill()

eight(60, True)
eight(80,False)

t.reset()
def draw_star(size, points):
    for x in range(0, points):
        t.forward(size)
        t.left(360//points)

draw_star(50, 12)
draw_star(50,24)
