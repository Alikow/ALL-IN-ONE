import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard

screen = Screen()
screen.screensize(600, 600)
screen.tracer(0)

cars = CarManager()
player = Player()
level = ScoreBoard()

screen.listen()
screen.onkeypress(player.go_up, "Up")

is_on = True
while is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_car()
    cars.move_car()

    # Collision with the car
    for car in cars.all_cars:
        if car.distance(player) < 20:
            level.game_over()
            is_on = False

    # At Finshe line
    if player.at_endline():
        player.goto_start()
        cars.level_up()
        level.level_up()

screen.mainloop()