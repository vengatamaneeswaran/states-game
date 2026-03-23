import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("India State Game")

# Image dimensions
img_width = 516
img_height = 600

# Setup physical window
# This creates the window on your monitor
screen.setup(width=img_width, height=img_height)

# Setting canvas size
# This ensures the 'drawing area' isn't bigger or smaller than the window
screen.screensize(canvwidth=img_width, canvheight=img_height)

# Set the background image
screen.bgpic("india-states-map.gif")

# To get coordinates for locations
# def get_mouse_click_coord(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coord)
# turtle.mainloop()

data = pd.read_csv("28_states.csv")
all_states = data.state.to_list()


state_list = []

while len(state_list) < 28:
    answer = screen.textinput(f"{len(state_list)}/28 States correct", "Enter a state").title()
    if answer == "Quit":
        missing_states = [state for state in all_states if state not in state_list] 
        new_data = pd.DataFrame(missing_states, columns=["state"])
        new_data.to_csv("states_to_learn.csv")
        break
    elif answer in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer, font=("Arial", 8, "bold"))
        state_list.append(answer)
