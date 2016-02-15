import turtle

t = turtle.Pen()

def mysquare(size):
    for x in range(1, 5):
        t.forward(size)
        t.left(90)

mysquare(80)

t.reset()
mysquare(25)
mysquare(50)
mysquare(75)
mysquare(100)
mysquare(125)

