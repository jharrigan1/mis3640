from session4 import arc, circle, move, polygon
import turtle
import math

#3.1.1

alex = turtle.Turtle()
alex.speed(0)

#large circle
circle(alex, 100)

#4 triangles
move(alex, 0, 100)
alex.setheading(60)
polygon(alex, 3, 100)
alex.setheading(150)
polygon(alex, 3, 100)
alex.setheading(240)
polygon(alex, 3, 100)
alex.setheading(330)
polygon(alex, 3, 100)

#4 small circles
moving_step = 50 * math.sqrt(3)
small_radius = 50 * math.sqrt(3) / 3

move(alex, 0, 100 - moving_step)
alex.setheading(180)
circle(alex, small_radius)

move(alex, -moving_step, 100)
alex.setheading(270)



