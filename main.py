from turtle import Turtle, Screen
import random
import time
from snake import Snake

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("That One Game")
screen.tracer(0)

snake_parts = []
snake_part_padding = 20


def make_apple():
    apple = Turtle("circle")
    apple.color("red")
    apple.penup()
    apple_xpos = random.randrange(int(-SCREEN_WIDTH / 2) + snake_part_padding,
                                  int(SCREEN_WIDTH / 2) - snake_part_padding,
                                  snake_part_padding)
    apple_ypos = random.randrange(int(-SCREEN_HEIGHT / 2) + snake_part_padding,
                                  int(SCREEN_HEIGHT / 2) - snake_part_padding,
                                  snake_part_padding)
    apple.goto(apple_xpos, apple_ypos)
    return apple

def hit_apple():
    if snake_parts[0].pos() == apple.pos():
        return True

apple = make_apple()
is_running = True
snake = Snake()
while is_running:
    snake.move()
    screen.update()
    time.sleep(0.1)
    screen.listen()

    screen.onkeypress(key="Up", fun=snake.move_up)
    screen.onkeypress(key="Down", fun=snake.move_down)
    screen.onkeypress(key="Left", fun=snake.move_left)
    screen.onkeypress(key="Right", fun=snake.move_right)
