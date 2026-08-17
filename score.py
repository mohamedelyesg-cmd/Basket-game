from turtle import Turtle
class Score:
    def __init__(self):
        self.turtle=Turtle()
        self.score=0
        self.turtle.color("red")
        self.turtle.hideturtle()
        self.turtle.penup()
        self.turtle.goto(0,240)
        self.writing()
    def writing(self):
        self.turtle.clear()
        self.turtle.write(self.score,font=("courier",30,"normal"),align="center")
    def game_over(self,color,message):
        self.turtle.goto(0,0)
        self.turtle.color(color)
        self.turtle.write(message,font=("Arial",35,"normal"),align="center")
