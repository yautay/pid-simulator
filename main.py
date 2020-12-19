from resources.model import Model
from resources.battery import Battery
from resources.propeller import Propeller
from resources.environment import Environment

env = Environment()   # std atmo
prop = Propeller(diameter=5.1, pitch=4.1)
bat = Battery(cells_no=4, capacity=1600, chemistry="lipo")
model = Model(mass=0.8, motors=4, motor_kv=1750, propeller=prop, battery=bat, environment=env)

t = model.test(1300, 0)
print(t)
