"""Test Road Rage Simulation"""
from car import *
import random
# from simulation import *

def test_car_obj_has_attributes():
    starting_position = [0, 0]
    car = Car(starting_position)
    assert car.position == [0, 0]
    assert car.acceleration_speed == 2

def test_car_moves_forward():
    car = Car([0, 0])
    car.move_forward()
    assert car.position == [2, 1]

def test_car_slows_down():
    car = Car([10, 4])
    car.acceleration_speed = 6
    car.slow_down()
    assert car.position == [16, 5]
    assert car.acceleration_speed == 4
