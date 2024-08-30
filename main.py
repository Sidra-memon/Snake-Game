# from turtle import *
# import turtle as t
# # Creating a window screen
# scr = t.Screen()
# scr.title("Snake Game")
# scr.bgcolor("black")
# # the width and height can be put as user's choice
# scr.setup(width=600, height=600)
# # set turtle screen title
# t.title("My Snake Game")
# scr.tracer(0)
# scr.exitonclick()

from turtle import Screen
import time
from snake import Snake
from food import Food
from Score_board import Scoreboard
# Screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
#Initializing Game Object
snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
# Game Loop
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail
    # for segment in snake.segments[1:]:
    #     if snake.head.distance(segment) < 10:
    #         game_is_on = False
    #         scoreboard.game_over()

screen.exitonclick()