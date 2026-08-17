from turtle import Screen
from basket import Basket
from item import Item
from score import Score
from time import *
t_s=0.1
window=Screen()
window.bgcolor("light blue")
window.setup(965,600)
window.listen()
window.tracer(0)
basket=Basket()
item=Item()
score=Score()
window.onkey(basket.right,"Right")
window.onkey(basket.left,"Left")
y=-15
while -15 < score.score < 15:
    item.goto(item.xcor(),item.ycor()+y)
    if item.ycor()<=-235 and item.distance(basket)<=70:
        item.hideturtle()
        if item.color()[0]=="yellow":
            score.score+=5
        elif item.color()[0]=="green":
            score.score+=3
        elif item.color()[0]=="red":
            score.score+=2
        else:
            score.score-=1
        item=Item()
        if y!=-31:
            y+=-2
    if item.ycor()<=-310:
        item.hideturtle()
        if item.color()[0]=="yellow":
            score.score-=12
        elif item.color()[0]=="black":
            score.score-=5
        elif item.color()[0]=="magenta":
            score.score-=3
        elif item.color()[0]=="blue":
            score.score-=2
        else:
            score.score-=1
        item=Item()
        if y!=-31:
            y+=-2
    score.writing()
    window.update()
    sleep(t_s)

if score.score>=15:
    if score.score==15:
        score.game_over("green",f"You Win😎\nYour score is: {score.score} = 15")
    else:
        score.game_over("green",f"You Win😎\nYour score is: {score.score} > 15")
else:
    if score.score==-15:
        score.game_over("red",f"You lose😭\nYour score is: {score.score} = -15")
    else:
        score.game_over("red",f"You lose😭\nYour score is: {score.score} < -15")
window.exitonclick()
