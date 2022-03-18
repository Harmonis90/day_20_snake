import random
import turtle
from snake import UNIT_SIZE
from turtle import Turtle

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600


class Apple(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("red")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        apple_xpos = random.randrange(int(-SCREEN_WIDTH / 2) + UNIT_SIZE,
                                      int(SCREEN_WIDTH / 2) - UNIT_SIZE,
                                      UNIT_SIZE)
        apple_ypos = random.randrange(int(-SCREEN_HEIGHT / 2) + UNIT_SIZE,
                                      int(SCREEN_HEIGHT / 2) - UNIT_SIZE,
                                      UNIT_SIZE)
        self.goto(apple_xpos, apple_ypos)



