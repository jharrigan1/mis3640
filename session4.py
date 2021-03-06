import turtle

alex = turtle.Turtle()

print(alex)

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

square(alex, 200)

def polygon(t, n, length):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)

polygon(alex, 3, 50)

import math

def circle(t, r):
    circumference = 2 * math.pi * r
    n = 75
    length = circumference / n
    polygon(t, n, length)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + l
    step_length = arc_length / n
    step_angle = angle / n
    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)

circle(alex, 75)

arc(alex, 100, 180)   
turtle.mainloop



def polyline(t, n, length, angle):
    """
    Draws n line segments with the given length and
    angle (in degrees) between them.  t is a turtle.

    """
    for i in range(n):
        t.fd(length)
        t.lt(angle)
   
def polygon(t, n, length):
    angle = 360.0 / n
    polyline(t, n, length, angle)

polygon(alex, 4, 100)
polyline(alex, 4, 100, 90)

turtle.mainloop()