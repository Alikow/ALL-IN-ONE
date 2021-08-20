from turtle import Turtle

START_PS = (0, -280)
MOVE_DIST = 10
FINISH_LINE_Y =280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.pu()
        self.goto_start()
        self.setheading(90)

    def go_up(self):
        self.forward(MOVE_DIST)

    def goto_start(self):
        self.goto(START_PS)

    def at_endline(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
