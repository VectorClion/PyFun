#!/usr/bin/python3
"""
    Author: Ves
    Feature: Painting a fractal tree by recursion
    Version: 1.0
    Date: 03/12/2017
"""

import turtle


def draw_branch(branch_length, floor):
    """
        Painting a fractal tree
    """
    step = 15

    if floor == 0:
        global n
        n = 1 + branch_length // step

    if branch_length >5:
        # Painting right branches
        if floor > n - 3:
            turtle.color('green')
        else:
            turtle.color('brown')
        turtle.pensize(n - floor)
        turtle.fd(branch_length)
        turtle.rt(20)
        floor += 1
        draw_branch(branch_length - step, floor)

        # Painting left branches
        turtle.lt(40)
        draw_branch(branch_length - step, floor)

        # the branch before return
        turtle.rt(20)
        floor -= 1
        if floor > n - 3:
            turtle.color('green')
        else:
            turtle.color('brown')
        turtle.pensize(n - floor)
        print(n, floor)
        turtle.bk(branch_length)


def main():
    """
        main program
    """
    floor = 0
    size = 100
    turtle.lt(90)
    turtle.pu()
    turtle.bk(150)
    turtle.pd()
    draw_branch(size, floor)
    turtle.exitonclick()


if __name__ == "__main__":
    main()






