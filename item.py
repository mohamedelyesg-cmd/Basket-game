from turtle import Turtle
from random import *
shapes=("circle","square","triangle","arrow","classic")
colors=("black","black","red","red","red","red","red","red","yellow","green","green","green","green","green","green","blue","blue","blue","blue","blue","blue","magenta","magenta","magenta","magenta","magenta")
class Item(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color(choice(colors))
        self.shape(choice(shapes))
        self.goto(randint(-460,460),310)
