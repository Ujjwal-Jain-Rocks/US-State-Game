import turtle
import pandas

screen = turtle.Screen()
screen.title("US State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data["state"].to_list()
x = data["x"].to_list()
y = data["y"].to_list()

turtle = turtle.Turtle()
turtle.penup()
turtle.hideturtle()

guess = []

while len(guess) < 50:
    answer = screen.textinput(title=f" {len(guess)}/50 Guess the state", prompt="What's another state's name?").title()
    if answer in states:
        index = states.index(answer)
        turtle.goto(x[index], y[index])
        guess.append(answer)
        turtle.write(states[index], align="center", font=("Arial", 10, "normal"))


screen.exitonclick()