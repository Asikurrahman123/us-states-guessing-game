import turtle

screen = turtle.Screen()
screen.setup(width=800, height=600)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

import pandas
data = pandas.read_csv("50_states.csv")
state_list = data.state.to_list()
guessing_state = []

while len(guessing_state) < 50:
    answer_state = screen.textinput(f"{len(guessing_state)}/50 totaled guessed states",
                                    prompt="What's the another state name").title()


# Using list comprehension


    if answer_state == "Exit":
        # missing_state = []
        # for state in state_list:
        #     if state not in guessing_state:
        #         missing_state.append(state)
        missing_state = [state for state in state_list if state not in guessing_state]
        missing_states = pandas.DataFrame(missing_state)
        missing_states.to_csv("missing_state.csv")
        break

    elif answer_state in state_list:
        guessing_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_name = data[data.state == answer_state]
        x = state_name.x
        y = state_name.y
        t.goto(int(x), int(y))
        t.write(answer_state, align="center", font=("Arial", 12, "normal"))


