from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.whole_snake = []
        self.positions = STARTING_POSITIONS
        self.create_snake()
        self.head = self.whole_snake[0]
        self.tail = self.whole_snake[-1]

    def create_snake(self):
        for position in self.positions:
            self.add_snake(position)

    def add_snake(self, position):
        self.snake = Turtle(shape='square')
        self.snake.penup()
        self.snake.setposition(position)
        self.snake.color("white")
        self.whole_snake.append(self.snake)

    def grow_snake(self):
        self.add_snake(self.whole_snake[-1].pos())

    def move(self):
        for snake_num in range(len(self.whole_snake) - 1, 0, -1):
            self.x_position = self.whole_snake[snake_num - 1].xcor()
            self.y_position = self.whole_snake[snake_num - 1].ycor()
            self.whole_snake[snake_num].goto(self.x_position, self.y_position)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def reset(self):
        for _ in self.whole_snake:
            _.setpos(1000, 1000)
        self.whole_snake.clear()
        self.create_snake()
        self.head = self.whole_snake[0]




