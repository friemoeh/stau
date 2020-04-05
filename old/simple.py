from random import randrange
from Car import Car

car1 = Car("Porsche Cayman S",15, 250)

car1.drive(100)

for t in range(10):
    print (t)
    print(car1)
    a=randrange(1,4)

    if a == 1:
        car1.brake(5)
        print("breaking")

    elif a == 2:
        car1.acc(5)
        print("acceleratione")

    else:
        car1.acc(0)
        print("keep")


 
    car1.goForward(t)

