from turtle import Turtle, Screen
import time
from car import Car
from player import Player
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
screen.onkey(player.move, "Up")

cars = Car()
scoreboard = Scoreboard()

game = True
while game:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move()

    for car in cars.all_cars:
        if car.distance(player) < 20:
            game = False
            scoreboard.game_over()

    if player.is_at_finish_line():
        player.goto_start()
        cars.level_up()
        scoreboard.increase_score()



screen.exitonclick()