import turtle
import random


is_race_on = False
screen = turtle.Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make Your Bet", prompt="Which turtle will win the race? Pick a colour: ")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
all_turtles = []

y = -150
for turtle_index in range (0, 6):
 new_turtle = turtle.Turtle(shape='turtle')
 new_turtle.color(colors[turtle_index])
 new_turtle.penup()
 new_turtle.setposition(x= -230, y= y)
 y += 50
 all_turtles.append(new_turtle)

if user_bet:
 is_race_on = True

while is_race_on:
 for new_turtle in all_turtles:
  new_turtle.forward(random.randint(0, 10))
  if new_turtle.xcor() > 230:
   is_race_on = False
   first = new_turtle.pencolor()
if user_bet == first:
 print(f"You've Won! The {first} turtle was the winner")
else:
 print(f"You Lost! The {first} turtle was the winner")


# tim = turtle.Turtle(shape='turtle')
# tim.color(random.choice(colors))
# tim.penup()
# tim.setposition(x=-240,y=150)

# def move_forwards():
#  tim.forward(100)
#
# screen.listen()
# screen.onkey(key="space", fun=move_forwards)

# def move_forward():
#  tim.forward(10)
#
# def move_backward():
#  tim.backward(10)
#
#
# def clockwise():
#  tim.right(10)
#
# def counter_clockwise():
#  tim.left(10)
#
#
# def clear():
#  tim.clear()
#  tim.penup()
#  tim.home()
#  tim.pendown()
#
# screen.listen()
# screen.onkey(fun = move_forward, key = "w")
# screen.onkey(fun = move_backward, key = "s")
# screen.onkey(fun = clockwise, key = "d")
# screen.onkey(fun = counter_clockwise, key = "a")
# screen.onkey(fun = clear, key = "c")


screen.exitonclick()
