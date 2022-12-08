import turtle as t
import math
tao = t.Pen()
t.color('red', 'blue')
for i in range(4):
    t.penup()
    t.fd(300)
    t.lt(90)
    t.fd(450)
    t.lt(90)
    t.pendown()
    t.begin_fill()
    t.circle(150)
    t.end_fill()
    t.penup()
    t.rt(90)
    t.goto(0, 0)
t.color('black', 'black')
for k in range(4):
    t.fd(300)
    t.lt(90)
    t.fd(150)
    t.rt(135)
    t.pendown()
    t.begin_fill()
    for j in range(4):
        t.fd(150 * math.sqrt(2))
        t.rt(90)
    t.end_fill()
    t.lt(135)
    t.penup()
    t.goto(0, 0)
t.color('green', 'orange')
for i in range(4):
    for k in range(2):
        t.fd(450)
        t.lt(90)
    t.pendown()
    for j in range(4):
        t.fd(300)
        t.lt(90)
    t.rt(90)
    t.penup()
    t.goto(0, 0)
t.color('black', 'black')
t.goto(0, -150)
n = 10
t.pendown()
while n <= 150 :
    t.circle(n)
    n += 10
