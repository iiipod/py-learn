import turtle

t = turtle.Pen()

t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)

t.reset()
for x in range(1, 20):
    t.forward(100)
    if x % 2 ==0:
        t.left(175)
    else:
        t.left(225)

t.reset()
t.color(1, 1, 0)
t.begin_fill()
t.circle(100)
t.end_fill()
