"""simulation class"""
from car import *
import numpy as np

class Simulation():
    """Will collaborate with car,
       will generate cars and track position of all cars"""
    def __init__(self):
        self.road_length = 1000
        self.car_list = []
        self.cars_on_road = 30

    def generate_starting_positions(self):
        x = 0
        starting_positions = np.linspace(0, self.road_length -1, \
            (self.road_length / 1000 * self.cars_on_road))
        return starting_positions

    def generate_cars(self, starting_positions):
        for pos in starting_positions:
            self.car_list.append(Car(pos))
        return self.car_list

    def move_cars(self):
        for car in self.car_list:
            car.move_forward()

    def look_ahead(self, car1, car2):
        next_move = (car1.position + car1.speed + car1.acceleration_speed)
        rotated = self.car_list[-1:], self.car_list[:-1]
        for car1, car2 in zip(self.car_list, rotated):
            if car2.position < car1.length + car1.postion:
                car1.stop()
            elif car2.position < car1.length + next_move:
                car1.slow_down()
            elif car2.position == car1.length + next_move:
                car1.match_speed()
            else:
                car1.move_forward()
        car2.move_forward()
            # elif car2.
