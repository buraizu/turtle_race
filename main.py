import turtle
from turtle import Turtle, Screen
import random

my_turtle = Turtle()
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
is_race_on = False
all_turtles = []


def setup_race():
    y_pos = -125
    for x in range(len(colors)):
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(colors[x])
        new_turtle.penup()
        new_turtle.goto(x=-230, y=y_pos)
        y_pos += 50
        all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True
    setup_race()

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()
