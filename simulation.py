"""simulation class"""
from car import *

class Simulation():
    """Will collaborate with car,
       will generate cars and track position of all cars"""
    def __init__(self):
        self.road_length = 1000
        self.car_list = []

    def generate_starting_positions(self):
        x = 0
        y = 0
        starting_positions = []
        for _ in range(30):
            starting_positions.append([x, y])
            x += 1000 / 30
        return starting_positions

    def generate_cars(self, starting_positions):
        for pos in starting_positions:
            self.car_list.append(Car(pos))
        return self.car_list    
