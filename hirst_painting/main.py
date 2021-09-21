import colorgram
import turtle as t
import random

#Extract 20 collors from the image
# colors = colorgram.extract('image.jpg', 30)
#
# color_list = []
# for color in colors:
#  red = color.rgb.r
#  green = color.rgb.g
#  blue = color.rgb.b
#  color_tuple = (red, green, blue)
#  color_list.append(color_tuple)
# print(color_list)

color_list = [(239, 223, 200), (203, 160, 115), (208, 224, 239), (242, 216, 229),
 (129, 168, 194), (212, 237, 224), (192, 143, 164), (133, 180, 158),
 (57, 106, 142), (220, 203, 130), (142, 71, 99), (151, 88, 57), (169, 158, 51),
 (59, 123, 92), (189, 89, 116), (227, 170, 189), (144, 21, 50), (75, 161, 131), (209, 91, 69),
 (156, 212, 191), (236, 171, 159), (67, 17, 42), (51, 163, 183), (17, 34, 70), (69, 21, 10),
 (177, 185, 221), (145, 210, 222), (106, 117, 172), (34, 53, 115), (14, 97, 58)]


tim = t.Turtle()

tim.home()
t.colormode(255)
t.speed('fastest')

def dot_line(dots):
 for i in range (dots):
  tim.setheading(0)
  tim.dot(20, random.choice(color_list))
  tim.penup()
  tim.forward(50)


def hirst_painting(dots):
 x= dots * (-20)
 y=  dots * (-20)
 tim.penup()
 tim.hideturtle()
 for i in range (dots):
  tim.setposition(x, y)
  dot_line(dots)
  y += 50


hirst_painting(10)

screen = t.Screen()
screen.exitonclick()

