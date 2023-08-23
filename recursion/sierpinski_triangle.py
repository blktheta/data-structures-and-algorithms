"""
The Sierpinski triangle illstrates a three-way recursive algorithm.

The procedure for drawing a Sierpinski triangle is simple.
    1. Start with a single large triangle.
    2. Divide this large triangle into four new triagles by connecting
    the midpoint of each side.
    3. Ignoring the middle triangle that you jst created, apply the
    same procedure to each of the corner triangles.
    4. Each time you create a new set of triangles, you recursively
    apply this procedure to the three smaller corner triangles.

Since the algorithm can be continued indefinetly, the base case
can be set as an arbitrarily number of times you want to divide the
triangle into pieces. This number can be called the degree, when we
reach a degree of 0, we stop.
"""
import turtle


def draw_triangle(points: list[tuple], color: str, t: turtle.Turtle):
    """Draw the triangles."""
    t.fillcolor(color)
    t.up()
    t.goto(points[0][0], points[0][1])
    t.down()
    t.begin_fill()
    t.goto(points[1][0], points[1][1])
    t.goto(points[2][0], points[2][1])
    t.goto(points[0][0], points[0][1])
    t.end_fill()


def get_mid(p1: tuple, p2: tuple) -> tuple:
    """Retrieve the point halfway between the endpoints."""
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)


def sierpinski(points: list[tuple], degree: int, t: turtle.Turtle):
    """Make the recursive call."""
    colormap = ["navy", "blue", "skyblue", "cyan", "turquoise", "lightgreen", "white"]
    draw_triangle(points, colormap[degree], t)
    if degree > 0:
        sierpinski(
            [points[0], get_mid(points[0], points[1]), get_mid(points[0], points[2])],
            degree - 1,
            t,
        )
        sierpinski(
            [points[1], get_mid(points[0], points[1]), get_mid(points[1], points[2])],
            degree - 1,
            t,
        )
        sierpinski(
            [points[2], get_mid(points[2], points[1]), get_mid(points[0], points[2])],
            degree - 1,
            t,
        )


def main():
    my_turtle = turtle.Turtle()
    my_win = turtle.Screen()
    my_points = [(-180, -150), (0, 150), (180, -150)]
    sierpinski(my_points, 5, my_turtle)
    my_win.exitonclick()


if __name__ == "__main__":
    main()
