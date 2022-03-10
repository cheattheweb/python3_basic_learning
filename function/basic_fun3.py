import turtle


def draw_tri(len):
    for i in range(3):
        turtle.forward(len)
        turtle.left(120)

n = input("Enter the length: ")
n = int(n)
draw_tri(n)

turtle.exitonclick()
