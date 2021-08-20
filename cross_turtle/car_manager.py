from turtle import Turtle
import random

COLORS = ["red", "blue", "green", "yellow", "orange", "purple"]
START_MOVE_DIS = 5
MOVE_INCREMENT = 10

class CarManager():
    def __init__(self):
        self.all_cars = []
        self.speed = START_MOVE_DIS
        
    def create_car(self):
        chance = random.randint(1, 6)
        if chance == 1:
            newcar = Turtle()
            newcar.pu()
            newcar.shape("square")
            newcar.shapesize(1, 2)
            newcar.color(random.choice(COLORS))
            newcar.goto(300, random.randrange(-250, 250))
            newcar.setheading(180)
            self.all_cars.append(newcar)

    def move_car(self):
        for car in self.all_cars:
            #self.backward(START_MOVE_DIS)
            car.forward(self.speed)

    def level_up(self):
        self.speed += MOVE_INCREMENT
