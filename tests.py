"""Test Road Rage Simulation"""
from car import *
import random
from simulation import *
import numpy as np

def test_car_obj_has_attributes():
    starting_position = 0
    car = Car(starting_position)
    assert car.position == 0
    assert car.acceleration_speed == 2

def test_car_moves_forward():
    car = Car(0)
    car.move_forward()
    assert car.position == 2

def test_car_slows_down():
    car = Car(10)
    car.acceleration_speed = 6
    car.slow_down()
    assert car.position == 16
    assert car.acceleration_speed == 4

def test_car_stops():
    car = Car(14)
    car.acceleration_speed = 12
    car.stop()
    assert car.acceleration_speed == 2
    assert car.position == 14

def test_sim_class_has_road():
    sim = Simulation()
    assert sim.road_length == 1000

def test_create_starting_positions():
    sim = Simulation()
    starting_positions = sim.generate_starting_positions()
    assert starting_positions.size == 30
    assert starting_positions[0] == 0

def test_sim_generates_30_cars():
    sim = Simulation()
    car_list = sim.generate_cars(sim.generate_starting_positions())
    car = car_list[0]
    assert len(sim.car_list) == 30
    assert type(car) == Car

def test_move_cars():
    sim = Simulation()
    car_list = sim.generate_cars(sim.generate_starting_positions())
    car = car_list[0]
    sim.move_cars()
    assert car.position == 2
    sim.move_cars()
    assert car.position == 6

def test_look_ahead():
    sim = Simulation()
    car1 = Car(10)
    car2 = Car(12)
    sim.look_ahead(car1, car2)
    assert car1.position < car2.position

def test_look_ahead_for_crash():
    sim = Simulation()
    car1 = Car(10)
    car2 = Car(11)
    sim.look_ahead(car1, car2)
    assert car1.position < car2.position
    assert car1.acceleration_speed == 2
    assert car1.position == 10
    assert car2.position == 13

    



sim = Simulation()
# car_list = sim.generate_cars(sim.generate_starting_positions())
car1 = Car(10)
car2 = Car(11)
sim.look_ahead(car1, car2)
print(car1.acceleration_speed)
print(car2.acceleration_speed, car2.position)
