import turtle

t = turtle.Pen()
t.color(1, 0.7, 1)

def mysquard(size, filled):
    if filled == True:
        t.begin_fill()
    for x in range(1, 5):
        t.forward(size)
        t.left(90)
    if filled == True:
        t.end_fill()

mysquard(85, True)

mysquard(150, False)
