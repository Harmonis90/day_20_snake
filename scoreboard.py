from turtle import Turtle, Screen

ALIGNMENT = "center"
GAME_OVER_FONT = ("Monospace", 54, "normal")
FONT = ("Consolas", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.speed("fastest")
        self.goto(0, 265)
        self.color("white")
        self.update_scoreboard()
        self.ht()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score {self.score}", align=ALIGNMENT, font=FONT)

    def add_to_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over_text(self):
        self.penup()
        self.goto(0, 0)
        self.color("red")
        self.write("GAME OVER", align=ALIGNMENT, font=GAME_OVER_FONT)