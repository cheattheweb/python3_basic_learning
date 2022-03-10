import turtle


def draw_square(side_len):
    for i in range(4):
        turtle.forward(side_len)
        turtle.left(90)


for count in range(36):
    draw_square(100)
    turtle.right(10)

turtle.exitonclick()
