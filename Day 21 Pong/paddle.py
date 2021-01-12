from turtle import Turtle, Screen




class Paddle(Turtle):

    def __init__(self, positions, controls):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(positions)

        screen = Screen()

        screen.listen()
        screen.onkey(self.go_up, controls[0])
        screen.onkey(self.go_down, controls[1])

    def go_up(self):
        if self.ycor() < 250:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)
        else:
            self.goto(self.xcor(), 250)

    def go_down(self):
        if self.ycor() > -250:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)
        else:
            self.goto(self.xcor(), -250)
