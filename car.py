import random
from turtle import Turtle
COLOR= ["red", "blue", "green", "yellow", "black"]
STARTING_DISTANCE = 5
MOVE_INCREMENT = 10


class Car:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_DISTANCE

    def create_car(self):
        random_car = random.randint(0,6)
        if random_car == 1:
            new_cars= Turtle("square")
            new_cars.shapesize(stretch_len=2, stretch_wid=1)
            new_cars.penup()
            new_cars.color(random.choice(COLOR))
            random_y = random.randint(-250, 250)
            new_cars.goto(300, random_y)
            self.all_cars.append(new_cars)

    def move(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT