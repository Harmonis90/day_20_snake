from scoreboard import ScoreBoard
from turtle import Turtle, Screen
from apple import Apple
from snake import Snake, UNIT_SIZE
import time


SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
sprite_size = UNIT_SIZE

screen = Screen()
scoreboard = ScoreBoard()

screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)

screen.bgcolor("black")
screen.title("That One Game")
screen.tracer(0)


def has_hit_wall():
    if snake.head.xcor() > int(SCREEN_WIDTH / 2) - sprite_size or \
            snake.head.xcor() < int(-SCREEN_WIDTH / 2) + sprite_size:
        return True
    elif snake.head.ycor() > int(SCREEN_HEIGHT / 2) - sprite_size or \
            snake.head.ycor() < int(-SCREEN_HEIGHT / 2) + sprite_size:
        return True


def has_hit_body():
    for part in snake.parts[1:]:
        if snake.head.distance(part.pos()) <= 0.01:
            print("hit")
            return True


def has_hit_apple(snake_obj, apple_obj):
    if snake_obj.distance(apple_obj.pos()) <= 0.01:
        return True


apple = Apple()
is_running = True
snake = Snake()
while is_running:

    screen.listen()
    screen.update()
    snake.move()
    has_hit_body()
    if has_hit_wall() or has_hit_body():
        scoreboard.game_over_text()
        is_running = False
    if has_hit_apple(snake.head, apple):
        apple.refresh()
        snake.add_part()
        scoreboard.add_to_score()
    screen.onkeypress(key="Up", fun=snake.move_up)
    screen.onkeypress(key="Down", fun=snake.move_down)
    screen.onkeypress(key="Left", fun=snake.move_left)
    screen.onkeypress(key="Right", fun=snake.move_right)
    time.sleep(0.1)
screen.exitonclick()
