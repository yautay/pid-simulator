import math


class Propeller:
    def __init__(self, diameter, pitch, efficiency_factor):
        self.__dia = diameter
        self.__pitch = pitch
        self.__ef = efficiency_factor

    def thrust(self, rpm, speed_fwd):
        d = self.__dia
        p = self.__pitch
        v0 = speed_fwd
        thrust = 4.39e-8*rpm*math.pow(d, 3.5)/math.sqrt(p)*(4.23e-4*rpm*p)-v0
        return thrust * self.__ef   # Newtons

    @property
    def diameter(self):
        return self.__dia

    @property
    def pitch(self):
        return self.__pitch
