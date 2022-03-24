import turtle
import pandas


screen = turtle.Screen()
screen.title("US States Guessing Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("50_states.csv")
all_states = data["state"].to_list()
guessed_state = []

while len(guessed_state) < 50:
    answer_state = screen.textinput(title="Guess the states in the US", prompt="Another one to go")

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_state:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("Your missing states")
        break
    if answer_state in all_states:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        selection = data[data["state"] == answer_state]
        t.goto(selection["x"], selection["y"])
        t.write(answer_state)

turtle.mainloop()