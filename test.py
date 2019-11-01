from random import randrange


#time in sec
t=0
n=1
vall = []

for car in range(1, 11):
    v=randrange(40, 50)
    vall.append((car,v))

for t in range(11):

    for car, v in vall :
        l=t*v
        print("car %d drove %d meters after %d seconds with the speed %d" %(car, l, t, v) )