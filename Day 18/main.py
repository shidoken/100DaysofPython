# import turtle
#
# tim = turtle.Turtle()
# screen = turtle.Screen()
# screen.exitonclick()

##########################

# from turtle import *
# from random import *
#
# choice([1, 2, 3])
# forward(100)

# from turtle import Turtle, Screen
# import random
#
# tim = Turtle()
# tim.shape("turtle")
# tim.color("red")
# tim.up()
# print(tim.goto(0,200))
# tim.down()
# tim.speed(2)
#
# tint = ['red', 'black', 'blue', 'green', 'purple', 'pink',
#         'grey', 'orange']
#
# def draw_shape(sides):
#     angle = 360 / sides
#     for _ in range(sides):
#         tim.forward(100)
#         tim.right(angle)
#
# for side_n in range(3,30):
#     tim.color(random.choice(tint))
#     draw_shape(side_n)
#
#
#
# screen = Screen()
# screen.exitonclick()


# for n in range(50):
#     for i in range(10):
#         tim.down()
#         tim.forward(10)
#         tim.up()
#         tim.forward(10)
#     tim.right(90)
#     if (n % 2 == 0):
#         tim.color("red")
#     else:
#         tim.color("blue")
#         tim.left(45)

import turtle
import random

# tom = Turtle()
# # tom.shape("turtle")
# turtle.pensize(10)


def change_color():
    R = random.random()
    B = random.random()
    G = random.random()

    turtle.color(R, G, B)


def cycle(num):
    if num == 1:
        turtle.forward(20)
        turtle.right(90)
    elif num == 2:
        turtle.forward(20)
        turtle.left(90)
    elif num == 3:
        turtle.back(20)
        turtle.right(90)
    elif num == 4:
        turtle.left(90)
        turtle.forward(20)

# while True:
#     x = random.randrange(1, 4)
#     change_color()
#     cycle(x)
directions = [0, 90, 180, 270]
turtle.speed(0)

# the command to make the turtle run at random
# while True:
#     change_color()
#     turtle.forward(30)
#     turtle.setheading(random.choice(directions))

# the command to make a spiralgraph

def slice_of_angle(angle):
    for x in range(int(360 / angle)):
        change_color()
        turtle.circle(100)
        turtle.setheading(turtle.heading() + angle)

slice_of_angle(5)


screen = turtle.Screen()
screen.exitonclick()

