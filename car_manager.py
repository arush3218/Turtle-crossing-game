from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            car_body = Turtle("square")
            car_body.shapesize(stretch_wid=1, stretch_len=2)
            car_body.penup()
            car_body.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            car_body.goto(300, random_y)
            
            car_window = Turtle("square")
            car_window.shapesize(stretch_wid=0.5, stretch_len=1.5)  
            car_window.penup()
            car_window.color("black")
            car_window.goto(car_body.xcor(), car_body.ycor() + 10)
            
            self.all_cars.append((car_body, car_window))

    def move_cars(self):
        for car_body, car_window in self.all_cars:
            car_body.backward(self.car_speed)
            car_window.goto(car_body.xcor(), car_body.ycor() + 10)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
