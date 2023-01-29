from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")

DIRECTORY = ".\\data.txt"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        with open(DIRECTORY) as data:
            self.high_score = int(data.read())
        self.score = 0
        self.color("white")
        self.goto(0, 270)

        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"Score : {self.score}  High score : {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(DIRECTORY, mode="w") as data_change:
                data_change.write(f"{self.high_score}")
        self.score = 0
        self.update_score()

    def curr_score(self):
        self.score += 1

        self.update_score()
