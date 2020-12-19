from resources.battery import Battery
from resources.propeller import Propeller
from resources.environment import Environment
from resources.motor import Motor
import math


class Model:
    def __init__(self, mass, motors, motor_kv, propeller, battery, environment):
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


    def test(self, command, v0):
        return self.__propeller.thrust(self.__motor.rpm(command, self.__battery.voltage(50)), v0)



    # @staticmethod
    # def __calc_lift_ratio(weight):
    #     power_lvl = np.linspace(0, 100, num=100, endpoint=True, dtype=int)
    #     lift_factor =
    #     return x
    #     # temp = time * time
    #     # f = interp1d(time, temp)
    #     # plt.plot(f(time))
    #     # plt.legend(['data', 'linear'], loc='best')
    #     # plt.show()
