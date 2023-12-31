"""
Simple example to illustrate the turtle module in Python.

Draw a spiral.

The base case is when the length of the line we want to draw, as given
by the len paramter, is reduced to zero or less.

If the length of the line is longer than zero, we instruct the turtle
to go forward by len units and then turn right 90 degrees.
"""
import turtle


def draw_spiral(my_turtle: turtle.Turtle, line_len: int):
    """Generate a spiral."""
    if line_len > 0:
        my_turtle.forward(line_len)
        my_turtle.right(90)
        draw_spiral(my_turtle, line_len - 5)


def main():
    my_turtle = turtle.Turtle()
    my_win = turtle.Screen()
    draw_spiral(my_turtle, 100)
    my_win.exitonclick()


if __name__ == "__main__":
    main()
