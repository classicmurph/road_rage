"""Define Car class with attributes and methods."""
import random


class Car():
    """Car will Collaborate with Simulation"""
    def __init__(self, starting_position):
        """construct car with these attributes"""
        self.position = starting_position
        self.acceleration_speed = 2
        self.deceleration_speed = 2
        self.max_speed = (120000//360)
        self.speed = 0
        self.size = 5

    def move_forward(self):
        self.position[0] += self.acceleration_speed
        self.position[1] += 1
        self.acceleration_speed += 2
        return self.position

    def slow_down(self):
        self.move_forward()
        self.acceleration_speed -= 4

    def stop(self):
        self.acceleration_speed = 2
        self.position[1] += 1
        return self.position

   
