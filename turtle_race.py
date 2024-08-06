import turtle as t
import random


# Define MyTurtle class inheriting from turtle.Turtle
class MyTurtle(t.Turtle):
    def __init__(self, color, position):
        super().__init__(shape="turtle")
        self.color(color)
        self.penup()
        self.goto(x=-250, y=position)


# Function to create a line
def create_line(start_x, start_y, end_x, end_y):
    line = t.Turtle()
    line.penup()
    line.goto(x=start_x, y=start_y)
    line.pendown()
    line.goto(x=end_x, y=end_y)
    line.hideturtle()
    return line


# Function to display a message on the screen
def display_message(message):
    message_turtle.clear()
    message_turtle.write(message, align="center", font=("Arial", 16, "normal"))


# Function to get full color name from user input
def get_color_from_input(user_input):
    for color_dict in colors:
        for full_color, variations in color_dict.items():
            if user_input in variations:
                return full_color
    return None


# Setup screen
screen = t.Screen()
screen.setup(width=900, height=500)

# Turtle configurations
turtle_color = ["Red", "Orange", "Yellow", "Pink", "Blue"]
turtle_position = [-100, -50, 0, 50, 100]

# Create starting line and finish line using the function
create_line(start_x=-230, start_y=150, end_x=-230, end_y=-150)
create_line(start_x=180, start_y=150, end_x=180, end_y=-150)

# Create a list of MyTurtle instances
turtles = []
for i in range(5):
    turtle = MyTurtle(turtle_color[i], turtle_position[i])
    turtles.append(turtle)

# Create a turtle for displaying messages
message_turtle = t.Turtle()
message_turtle.hideturtle()
message_turtle.penup()
message_turtle.goto(x=0, y=180)

# List of dictionaries to map colors to their possible inputs
colors = [
    {"Red": ["r", "red"]},
    {"Orange": ["o", "orange"]},
    {"Yellow": ["y", "yellow"]},
    {"Pink": ["p", "pink"]},
    {"Blue": ["b", "blue"]}
]

# Get user bet and validate input
user_bet = None
while user_bet is None:
    user_bet_input = screen.textinput(title="Make your bet", prompt="Who will win? Red/Orange/Yellow/Pink/Blue:")
    if user_bet_input is not None:
        user_bet_input = user_bet_input.lower()
        user_bet = get_color_from_input(user_bet_input)
    if user_bet is None:
        display_message("Invalid choice. Please select from (r/o/y/p/b or full color name).")

display_message(f"User bet on: {user_bet}")

# Initialize win_colour as a list
win_colour = []
race_on = True

# Start race
while race_on:
    for each in turtles:
        speed = random.randint(4, 7)
        each.forward(speed)

        if each.xcor() > 180:
            if each.pencolor() not in win_colour:
                win_colour.append(each.pencolor())

    if len(win_colour) > 0:
        race_on = False

# Check the total number of winners
total = len(win_colour)
# print(f"{total}:{win_colour}")

# Collect all messages to display
messages = []

# Determine the race outcome
if total > 1:
    messages.append("It's a draw between:")
    for color in win_colour:
        messages.append(f"{color} turtle")
else:
    winner = win_colour[0]
    if winner == user_bet:
        messages.append(f"Hoorah! You win. The {winner} turtle wins the race")
    else:
        messages.append(f"Nooo! The {winner} turtle wins. You lost the bet")

# Display all messages
display_message("\n".join(messages))

screen.exitonclick()
