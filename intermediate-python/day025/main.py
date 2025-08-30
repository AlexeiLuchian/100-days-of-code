import turtle, pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")

states_list = data["state"].to_list()
x_list = data["x"].to_list()
y_list = data["y"].to_list()

states_dict = {}
for i in range(len(states_list)):
    states_dict[states_list[i]] = (x_list[i], y_list[i])

correct_guesses = []
nr_of_correct_guesses = 0

game_on = True
text = turtle.Turtle()
text.hideturtle()
text.penup()

while game_on:
    answer = screen.textinput(title=f"{nr_of_correct_guesses}/50 States Correct", prompt="What's another state?")
    if answer:
        answer = answer.title()
        if answer in states_dict and answer not in correct_guesses:
            text.goto(states_dict[answer])
            text.write(answer)
            nr_of_correct_guesses += 1
            correct_guesses.append(answer)
    if answer == None or nr_of_correct_guesses == 50:
        game_on = False
    
states_to_learn = []
for state in states_dict:
    if state not in correct_guesses:
        states_to_learn.append(state)

new_dataframe = pandas.DataFrame(states_to_learn)
new_dataframe.to_csv('states_to_learn.csv')