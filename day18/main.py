import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.shape('arrow')
# colors = ['yellow', 'gold', 'orange', 'red', 'maroon', 'violet', 'magenta', 'purple', 'navy', 'blue',
#           'skyblue', 'cyan', 'turquoise', 'lightgreen', 'green', 'darkgreen',
#           'chocolate', 'brown', 'black', 'gray', 'DarkOrange4', "DarkSalmon"]

def random_color():
 r = random.randint(0,225)
 g = random.randint(0,255)
 b = random.randint(0,255)
 colors = (r, g, b)
 return colors



# for i in range(4):
#  tim.forward(100)
#  tim.right(90)

# for i in range (20):
#  tim.pendown()
#  tim.forward(10)
#  tim.penup()
#  tim.forward(10)



# sides = 11
#
# for i in range (3, sides):
#  tim.color(choice(colors))
#  tim.pendown()
#  for j in range (i):
#   tim.forward(70)
#   tim.right(360/i)
#  tim.penup()


# def draw_shape(sides):
#  angle = 360/sides
#  for i in range (sides):
#   tim.forward(100)
#   tim.right(angle)
#
#
# for i in range(3, 11):
#  tim.color(random.choice(colors))
#  tim.pendown()
#  draw_shape(i)
#  tim.penup()


def draw():
 tim.color(random_color())
 tim.pendown()
 tim.setheading(random.choice(angle))
 tim.forward(20)



# tim.pensize(8)
# tim.speed('fastest')
# for i in range (201):
# angle = [0, 90, 180, 270]
#  draw()



# def draw_circle(angle):
#  tim.color(random_color())
#  tim.circle(100)
#  tim.setheading(angle)


tim.speed(0)
def spirograph(size):
 for i in range (int(360/size)):
  tim.color(random_color())
  tim.circle(100)
  tim.setheading(tim.heading() + size)


spirograph(5)

screen = t.Screen()
screen.exitonclick()




