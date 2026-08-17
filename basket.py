from turtle import Turtle
class Basket(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.shapesize(1,7)
        self.color("purple")
        self.penup()
        self.goto(0,-250)
    def right(self):
        if self.xcor()<=380:
            self.goto(self.xcor()+50,self.ycor())
    def left(self):
        if self.xcor()>=-380:
            self.goto(self.xcor()-50,self.ycor())

