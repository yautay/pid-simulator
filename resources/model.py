import numpy as np

from resources.battery import Battery
from resources.propeller import Propeller
from resources.environment import Environment
from resources.motor import Motor
import math


class Model:
    def __init__(self, mass, motors, motor_kv, propeller, battery, environment, size):
        __bat = isinstance(battery, Battery)
        __prop = isinstance(propeller, Propeller)
        __env = isinstance(environment, Environment)
        if not __bat:
            print("battery is not instance of Battery class")
            raise Exception
        if not __prop:
            print("propeller is not instance of Propeller class")
            raise Exception
        if not __env:
            print("environment is not instance of Environment class")
            raise Exception

        self.__battery = battery
        self.__propeller = propeller
        self.__motors = motors
        self.__mass = mass
        self.__environment = environment
        self.__motor = Motor(motor_kv)
        self.__size = size
        self.__xy_coordinates = self.__get_coordinates()

    def __get_coordinates(self):
        arm = self.__size / math.sqrt(2) / 2000
        return np.array([[arm, -arm], [arm, arm], [-arm, arm], [-arm, -arm]], dtype="float16")
