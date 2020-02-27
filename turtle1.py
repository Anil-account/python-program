import turtle

# t=turtle.Turtle()
# t.forward(100)
# t.left(90)
# t.forward(50)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(50)
# turtle.done()

#to draw rectangle using loop
# t = turtle.Turtle()
# t.pencolor('red')
# for i in range(4):
#     t.forward(100)
#     t.left(90)
# t.left(45)
# t.forward(140)
#
# turtle.done()


# to make rectangle
t = turtle.Turtle()
# t.pencolor('red')
# for i in range(2):
#     t.forward(100)
#     t.left(90)
#     t.forward(50)
#     t.left(90)
#     # t.stamp()
#
# # to make circle
# t.begin_fill()
# t.shape('arrow')
# t.circle(10)
# t.forward(100)
# t.fillcolor('yellow')
# t.circle(10)
# t.stamp()


# to make small rectangle
t.end_fill()
t.penup()
t.goto(50,30)
t.pendown()
for i in range(4):
    t.forward(10)
    t.left(90)

# to make circle
# t.penup()
# t.goto(0,150)
# t.pendown()
# t.begin_fill()
# t.fillcolor('grey')
# t.circle(50)
# t.end_fill()

# to fill circle
# t.penup()
# t.goto(-200,0)
# t.pendown()
# for i in range(10):
#     t.circle(10*i)
#     t.up()
#     t.sety((10*i)*(-1))
#     t.down()
# t.goto(-200,100)


# to make hexagon
# t.pencolor('red')
# t.penup()
# t.goto(-500,-150)
# t.pendown()
# for i in range(12):
#     t.forward(50)
#     t.left(30)


# to make star


t.pencolor('red')
t.penup()
t.goto(-500,-150)
t.pendown()
for i in range(100):
    t.circle(10*i)





turtle.done()
