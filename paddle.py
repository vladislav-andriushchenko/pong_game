from turtle import Turtle

X_POS = 350
Y_POS = 0
WIDTH = 5
HEIGHT = 1
UP = 90
DOWN = 270
MOVE_STEP = 20


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.resizemode("user")
        self.turtlesize(stretch_wid=WIDTH, stretch_len=HEIGHT)
        self.color("white")
        self.penup()
        self.setposition(position)

    def move_up(self):
        new_y = self.ycor() + MOVE_STEP
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - MOVE_STEP
        self.goto(self.xcor(), new_y)
