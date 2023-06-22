"""
Rayyan Jamil
Turtle Etch-sketch
Mr. Dohmen
"""

import turtle
import random

canvas = turtle.Screen()
ray = turtle.Turtle()


def north():
    ray.seth(90)
    ray.fd(10)

def east():
    ray.seth(0)
    ray.fd(10)


def south():
    ray.seth(270)
    ray.fd(10)


def west():
    ray.seth(180)
    ray.fd(10)


def clear():
    ray.clear()


def dropBombs(t):
    for x in range(20):
        t.speed(10)
        t.color('red')
        t.pu()
        t.goto(random.randint(-500, 500), random.randint(-500, 500))
        t.dot(size = random.randint(50, 100))
        yDanger = t.ycor()
    

def main():
    dropBombs(ray)
    turtle.color("black")
    turtle.onkeypress(north, "w")
    turtle.onkeypress(east, "d")
    turtle.onkeypress(south, "s")
    turtle.onkeypress(west, "a")
    turtle.onkeypress(clear, "x")
    canvas.listen()

if (__name__=="__main__"):
    main()
