from turtle import Turtle

#  constant variables
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
#  constant variables


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        segment_snake = Turtle(shape="square")
        segment_snake.color("white")
        segment_snake.penup()  # 2 #
        segment_snake.goto(position)
        self.segments.append(segment_snake)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x=new_x, y=new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:  # making sure of direction is different from, the opposite direction
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:  # making sure of direction is different from, the opposite direction
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:  # making sure of direction is different from, the opposite direction
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:  # making sure of direction is different from, the opposite direction
            self.head.setheading(RIGHT)

