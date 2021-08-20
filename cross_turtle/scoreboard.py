from turtle import Turtle

FONT = ("courier", 20, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.pu()
        self.hideturtle()
        self.goto(-300, 240)
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"LEVEL: {self.score}", False, "left", FONT)

    def level_up(self):
        self.score +=1
        self.write_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, "center", FONT)
    