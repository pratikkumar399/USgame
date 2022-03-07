import turtle
import pandas as pd

screen = turtle.Screen()
screen.title('Us States Game')

image = "blank_states_img.gif"

screen.addshape(image)
screen.setup(height=491, width=725)
turtle.shape(image)

df = pd.read_csv('50_states.csv')
all_states = df.state.to_list()

answer_state = screen.textinput(
    title="Guess the State", prompt='What\'s another state name?')
print(answer_state)

while len(answer_state) < 50 :
    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = df[df.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())


# def get_mouse_click_coordinates(x,y):
#     print(x,y)

# turtle.onscreenclick(get_mouse_click_coordinates)

# turtle.mainloop()
screen.exitonclick()
