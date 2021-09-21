from turtle import Turtle, Screen


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.setpos(position)
        self.shape('square')
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color('white')


    def up(self):
        if self.ycor() < 870 or self.ycor() > -870:
            self.sety(self.ycor()+20)

    def down(self):
        if self.ycor() < 870 or self.ycor() > -870:
            self.sety(self.ycor()-20)


