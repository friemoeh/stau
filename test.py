from random import randrange

def bremsen(v, delta):
  if v<delta:
    return v
  return v-delta

def acc(v, delta):
  if v<maxV:
    return v+delta
  return v

# time in sec
t = 0
n = 1
vall = []
maxV = 100

for car in range(0, n):
  v = randrange(40, 50)
  vall.append((car, v))

for t in range(11):

  for car, v in vall:
    a=randrange(1,3)

    if a == 1:
        v = bremsen(v, 5)
    else:
        v = acc(v, 5)
        
    vall[car] = (car,v)
    l = t*v
    print("car %d drove %d meters after %d seconds with the speed %d" % (car, l, t, v))

