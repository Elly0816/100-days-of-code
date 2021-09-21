from turtle import Turtle


ALIGN = 'center'
FONT = ("Courier", 10, 'normal')
FONT2 = ("Courier", 20, 'normal')



class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.setposition(0, 285)
        self.color('white')
        self.point = 0
        with open('high_score.txt', 'r') as high_score:
            self.high_point = int(high_score.read())
        self.speed('fastest')
        self.hideturtle()

    def new_score(self):
        self.point += 1
        self.score()

    def score(self):
        self.clear()
        self.write(f"Score: {self.point}     High Score: {self.high_point}", False, align=ALIGN, font=FONT)


    def reset(self):
        if self.point > self.high_point:
            self.high_point = self.point
            with open("high_score.txt", 'w') as high_score:
                high_score.write(f"{self.high_point}")
        self.point = 0
        self.score()




