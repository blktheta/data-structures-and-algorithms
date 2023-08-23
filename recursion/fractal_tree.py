"""Simple example to illustrate visual recursion in Python.

Create an algorithm that generate a fractal tree.

By definition, a fractal has the same basic shape no matter how much you
magnify it. If we translate this to trees and shrubs, we might say that
even a small twig has the same shape and characteristics as a whole
tree. Using this idea we could say that a tree is a trunk, with a
smaller tree going off to the right and another smaller tree going off
to the left. If you think of this definition recursively, it means that
we will apply the recursive definition of a tree to both of the smaller
left and right trees.
"""
import turtle


def tree(branch_len: int, t: turtle.Turtle):
    """Generate a fractal tree."""
    if branch_len > 5:
        t.forward(branch_len)
        t.right(20)
        tree(branch_len - 15, t)
        t.left(40)
        tree(branch_len - 15, t)
        t.right(20)
        t.backward(branch_len)


def main():
    t = turtle.Turtle()
    display = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(75, t)
    display.exitonclick()


if __name__ == "__main__":
    main()
