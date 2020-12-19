class Environment:
    def __init__(self, temperature=15, pressure=1013.25, density=1.2255, elevation=0):
        self.__tmp = temperature
        self.__press = pressure
        self.__elev = elevation
        self.__dens = density

    @property
    def temperature(self):
        return self.__tmp

    @property
    def elevation(self):
        return self.__elev

    @property
    def pressure(self):
        return self.__press

    @property
    def density(self):
        return self.__dens
