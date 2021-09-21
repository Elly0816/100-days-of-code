from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
score = ScoreBoard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    score.score()

    snake.move()

#    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.new_score()
#   #Add snake segment for each food collision
        snake.grow_snake()

#   #Detect collision with wall
    x_bound = snake.head.xcor()
    y_bound = snake.head.ycor()

    if x_bound < -290 or x_bound > 290 or y_bound < -290 or y_bound > 285:
        score.reset()
        snake.reset()

#   #Detect collision with self
    for _ in snake.whole_snake[1:]:
        if snake.head.distance(_) < 10:
            score.reset()
            snake.reset()

screen.exitonclick()
