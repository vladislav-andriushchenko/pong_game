from turtle import Turtle

ALIGN = "center"
FONT = ('Courier', 80, 'bold')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.setposition(x=-100, y=195)
        self.write(self.l_score, font=FONT, align=ALIGN)
        self.setposition(x=100, y=195)
        self.write(self.r_score, font=FONT, align=ALIGN)

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()
