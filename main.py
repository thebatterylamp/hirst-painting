import random
import turtle as t
import colorgram

colors = colorgram.extract('image.jpg', 9)
t.colormode(255)
tim = t.Turtle()
tim.shape('arrow')
tim.color('green')
tim.speed('fast')
tim.width(5)


def random_color():
    color_set = [colors[0].rgb, colors[1].rgb, colors[2].rgb, colors[3].rgb, colors[4].rgb, colors[5].rgb,
                 colors[6].rgb, colors[7].rgb, colors[8].rgb]
    return random.choice(color_set)


shift = [(0.00, 0.00), (0.00, 30.00), (0.00, 60.00), (0.00, 90.00), (0.00, 120.00), (0.00, 150.00), (0.00, 180.00),
         (0.00, 210.00), (0.00, 240.00), (0.00, 270.00)]
shift_index = 0


def next_index():
    global shift_index
    if shift_index < 9:
        shift_index += 1
    return shift[shift_index]


cycle = 0
while cycle < 10:
    for _ in range(10):
        tim.hideturtle()
        tim.dot(10, random_color())
        tim.penup()
        tim.forward(30)
    tim.goto(next_index())
    cycle += 1

my_screen = t.Screen()
my_screen.screensize(300, 300)
my_screen.exitonclick()
