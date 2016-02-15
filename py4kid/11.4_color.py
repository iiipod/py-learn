import turtle

t = turtle.Pen()

def mycircle(red, green, blue):
    t.color(red, green, blue)
    t.begin_fill()
    t.circle(90)
    t.end_fill()

mycircle(0, 1, 0)

t.reset()
mycircle(0, 0.5, 0)

t.reset()
mycircle(1, 0, 0)

t.reset()
mycircle(0, 0, 0)

t.reset()
mycircle(1, 0.9, 1)
