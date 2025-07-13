# Turtle race 

from turtle import Turtle, Screen
import random

screen = Screen()
screen.title("Turtle race")
screen.setup(width=800, height=600)
colors = ("red", "blue", "green")
y = (-70, 0, 70)

turtles = []
user_bet = screen.textinput("Make your bet", "Guess the winner: \nType a color: Red, Blue, Green")

# If the user presses Cancel
if user_bet is None:
    screen.bye()
else:
    user_bet = user_bet.lower()
    
    for i in range(3):
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(colors[i])
        new_turtle.penup()
        new_turtle.goto(-380, y[i])
        turtles.append(new_turtle)

    def race_turtles():
        is_race_on = True
        while is_race_on:
            for turtle in turtles:
                if turtle.xcor() > 380:
                    is_race_on = False
                    winning_color = turtle.pencolor()
                    display_result(winning_color == user_bet)
                else:
                    turtle.forward(random.randint(1, 5))

    def display_result(is_winner):
        result_turtle = Turtle()
        result_turtle.hideturtle()
        result_turtle.penup()
        result_turtle.goto(0, 0)
        result_turtle.pendown()
        
        if is_winner:
            screen.bgcolor("dark green")
            result_turtle.color("white")
            result_turtle.write("You win!", align="center", font=("arial", 10, "bold"))
        else:
            screen.bgcolor("dark red")
            result_turtle.color("white")
            result_turtle.write("You lose!", align="center", font=("arial", 10, "bold"))

    race_turtles()

    screen.exitonclick()