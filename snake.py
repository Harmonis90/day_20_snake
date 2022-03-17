from turtle import Turtle

UNIT_SIZE = 20
START_XPOS = 0
START_YPOS = 0
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.parts = []
        self.init_snake()
        self.head = self.parts[0]

    def init_snake(self):
        current_xpos = START_XPOS
        for i in range(3):
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.goto(current_xpos, START_YPOS)
            current_xpos -= UNIT_SIZE
            self.parts.append(segment)

    def move(self):
        for index in range(len(self.parts) - 1, 0, -1):
            new_xpos = self.parts[index - 1].xcor()
            new_ypos = self.parts[index - 1].ycor()
            self.parts[index].goto(new_xpos, new_ypos)
        self.head.fd(UNIT_SIZE)

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)
