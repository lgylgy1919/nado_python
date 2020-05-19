import random
import inspect
from travel import *
from travel.thailand import ThailandPackage
from travel import vietnam
import travel.thailand
trip_to = travel.thailand.ThailandPackage()
trip_to.detail()

trip_to = ThailandPackage()
trip_to.detail()

trip__to = vietnam.VietnamPackage()
trip__to.detail()


trip_to = vietnam.VietnamPackage()
trip_to.detail()
trip__to = thailand.ThailandPackage()
trip__to.detail()

print(inspect.getfile(random))
print(inspect.getfile(thailand))
