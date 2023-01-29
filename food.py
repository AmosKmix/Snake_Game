import random
from turtle import Turtle


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("yellow")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-270, 270)
        random_y = random.randint(-270, 270)
        self.goto(x=random_x, y=random_y)


# my try without the learning and without the inheritance class -
# def __init__(self):
# my try without the learning and without the inheritance class -
# self.create_food()
# my try without the learning and without the inheritance class -
# self.location()
# my try without the learning and without the inheritance class -
# pass
# my try without the learning and without the inheritance class -
# my try without the learning and without the inheritance class -
# def create_food(self):
# my try without the learning and without the inheritance class -
# food = Turtle("square")
# my try without the learning and without the inheritance class -
# food.shapesize(0.5)
# my try without the learning and without the inheritance class -
# food.penup()
# my try without the learning and without the inheritance class -
# food.color("yellow")
# my try without the learning and without the inheritance class -
# food.setpos(x=random.randint(-280, 280), y=random.randint(-280, 280))
