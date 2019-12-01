class Car:
    def __init__(self, n, a, m):
        self.name = n
        self.age = a
        self.speed = 0
        self.maxspeed = m
        self.position = 0
        self.lastTime = 0

    def __str__(self):
        return "the %s is at position %d, and drives with the speed %d" % (self.name, self.position, self.speed)

    def drive(self, s):
        self.speed = s
        if s > self.maxspeed:
            self.speed = self.maxspeed

        if self.speed < 0:
            self.speed = 0

    def acc(self, a):
        self.drive(self.speed + a)

    def brake(self, b):
        new_speed = self.speed - b
        self.drive(new_speed)

    def goForward(self, t):  # t ist die ZEIT
        self.position = self.position + (t-self.lastTime) * self.speed
        self.lastTime = t


