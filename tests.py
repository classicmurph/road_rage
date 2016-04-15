"""Test Road Rage Simulation"""
from car import *
import random
from simulation import *

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

def test_car_stops():
    car = Car([14, 6])
    car.acceleration_speed = 12
    car.stop()
    assert car.acceleration_speed == 2
    assert car.position == [14, 7]

def test_sim_class_has_road():
    sim = Simulation()
    assert sim.road_length == 1000

def test_create_starting_positions():
    sim = Simulation()
    starting_positions = sim.generate_starting_positions()
    assert len(starting_positions) == 30
    assert starting_positions[0] == [0, 0]

def test_sim_generates_30_cars():
    sim = Simulation()
    car_list = sim.generate_cars(sim.generate_starting_positions())
    car = car_list[0]
    assert len(sim.car_list) == 30
    assert type(car) == Car
