from turtle import Screen,Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

my_screen=Screen()
my_screen.setup(600,600)
my_screen.bgcolor("black")
my_screen.title("Snake Game")
my_screen.tracer(0)

starting_positions=[(0,0),(-20,0),(-40,0)]

snake=Snake()
food=Food()
scoreboard=Scoreboard()

my_screen.listen()
my_screen.onkey(snake.up,"Up")
my_screen.onkey(snake.down,"Down")
my_screen.onkey(snake.right,"Right")
my_screen.onkey(snake.left,"Left")

game_is_on=True

while game_is_on:
    my_screen.update()
    snake.move()
    time.sleep(0.2) 
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        game_is_on=False
        scoreboard.game_over()
    for seg in snake.segments[1:]:
        if snake.head.distance(seg)< 10:
            game_is_on=False
            scoreboard.game_over()


my_screen.exitonclick()