#!/usr/bin/python
"""
    Author: Ves
    Feature: Painting a Pentagram
    Version: 1.0
    Date: 30/11/2017
"""
import turtle


def draw_pentagram(size):
    """
    painting pentagram
    """
    count = 1
    while count <= 5:
        turtle.forward(size)
        turtle.right(144)
        count = count + 1


def main():
    """
    main program
    """
    # size = eval(input('Initialize the distance: '))
    # n = 12
    # angle = 5
    # for i in range(0, n):
    #     for j in range(0, 5):
    #         turtle.forward(size + i * 10)
    #         turtle.right(144)

    turtle.width(5)
    turtle.color('black')
    # word 'H'
    turtle.pu()
    turtle.bk(350)
    turtle.rt(90)
    turtle.bk(50)
    turtle.pd()
    turtle.fd(100)
    turtle.pu()
    turtle.bk(50)
    turtle.lt(90)
    turtle.pd()
    turtle.fd(50)
    turtle.pu()
    turtle.rt(90)
    turtle.bk(50)
    turtle.pd()
    turtle.fd(100)

    # word 'E'
    turtle.pu()
    turtle.bk(50)
    turtle.lt(90)
    turtle.fd(10)
    turtle.pd()
    turtle.fd(50)
    turtle.lt(90)
    turtle.fd(50)
    turtle.lt(90)
    turtle.fd(50)
    turtle.lt(90)
    turtle.fd(100)
    turtle.lt(90)
    turtle.fd(50)

    # double 'l'
    turtle.pu()
    turtle.fd(10)
    turtle.rt(90)
    turtle.bk(100)
    turtle.pd()
    turtle.fd(100)
    turtle.lt(90)
    turtle.fd(50)

    turtle.pu()
    turtle.fd(10)
    turtle.rt(90)
    turtle.bk(100)
    turtle.pd()
    turtle.fd(100)
    turtle.lt(90)
    turtle.fd(50)

    # word 'O'
    turtle.pu()
    turtle.fd(10)
    turtle.rt(90)
    turtle.bk(100)
    turtle.pd()
    turtle.fd(100)
    turtle.lt(90)
    turtle.fd(50)
    turtle.lt(90)
    turtle.fd(100)
    turtle.lt(90)
    turtle.fd(50)

    # word 'W'
    turtle.pu()
    turtle.bk(70)
    turtle.lt(105)
    turtle.pd()
    turtle.fd(106)
    turtle.lt(150)
    turtle.fd(106)
    turtle.rt(150)
    turtle.fd(106)
    turtle.lt(150)
    turtle.fd(106)

    # word 'O'
    turtle.pu()
    turtle.rt(75)
    turtle.fd(10)
    turtle.rt(90)
    turtle.pd()
    turtle.fd(100)
    turtle.lt(90)
    turtle.fd(50)
    turtle.lt(90)
    turtle.fd(100)
    turtle.lt(90)
    turtle.fd(50)

    # word 'R'
    turtle.pu()
    turtle.bk(60)
    turtle.lt(90)
    turtle.pd()
    turtle.fd(100)
    turtle.pu()
    turtle.bk(100)
    turtle.lt(90)
    turtle.pd()
    turtle.fd(50)
    turtle.rt(90)
    turtle.fd(50)
    turtle.rt(90)
    turtle.fd(50)
    turtle.lt(135)
    turtle.fd(72)

    # word 'L'
    turtle.pu()
    turtle.lt(45)
    turtle.fd(10)
    turtle.rt(90)
    turtle.bk(100)
    turtle.pd()
    turtle.fd(100)
    turtle.lt(90)
    turtle.fd(50)

    # word 'D'
    turtle.pu()
    turtle.fd(10)
    turtle.rt(90)
    turtle.bk(100)
    turtle.pd()
    turtle.fd(100)
    turtle.pu()
    turtle.bk(100)
    turtle.lt(90)
    turtle.bk(2)
    turtle.pd()
    turtle.fd(52)
    turtle.rt(90)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(52)

    turtle.penup()
    turtle.backward(70)
    turtle.right(90)
    turtle.forward(100)
    turtle.pendown()
    turtle.pensize(1)
    turtle.pencolor('red')

    size = 50
    while size <= 80:
        # call function
        draw_pentagram(size)
        size += 10

    turtle.exitonclick()


if __name__ == "__main__":
    main()
