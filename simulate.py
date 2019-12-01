from random import randrange
from Car import Car

car1 = Car("Porsche Cayman S",15, 250)

car1.drive(100)

for t in range(10):
    print (t)
    print(car1)
    a=randrange(1,3)

    if a == 1:
        car1.brake(5)
        print("breaking")

    else:
        car1.acc(5)
        print("acceleratione")

    car1.goForward(t)

