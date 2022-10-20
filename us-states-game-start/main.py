import turtle
import pandas
count = 0
data = pandas.read_csv("50_states.csv")
list_of_states = data["state"].to_list()
correct_guesses = []
states_to_learn = []

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
##Code req to make 50_states.csv file
# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()
#
# screen.exitonclick()
while count != 50:
    if count == 0:
        text = "Guess the State"
    else:
        text = f"{count}/50 States Guessed"
    answer_state = screen.textinput(title=f"{text}", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        break
    if answer_state in correct_guesses:
        print("You've already guessed that.")
    if answer_state in list_of_states:
        state_data = data[data.state == f"{answer_state}"]
        x_cor = int(state_data.x)
        y_cor = int(state_data.y)
        state = turtle.Turtle()
        state.hideturtle()
        state.penup()
        state.goto(x=x_cor, y=y_cor)
        state.write(f"{answer_state}", align='center', font=("Times New Roman", 12, 'bold'))
        count = count + 1
        correct_guesses.append(answer_state)

#Creating a states_to_learn.csv file
for item in list_of_states:
    if item not in correct_guesses:
        states_to_learn.append(item)
data2 = pandas.DataFrame(states_to_learn)
data2.to_csv("states_to_learn.csv")







