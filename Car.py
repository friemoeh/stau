from random import random

class Car:
    def __init__(self, x, lap, startvelocity=0, randomization=0.5):
        self.position = x
        self.lap = lap
        self.default_acc=1
        self.velocity = startvelocity
        self.randomization=randomization
        self.max_acceleration = 5.0
        self.max_velocity = 20
        self.brake_deceleration = 10
        self.free_deceleration = 2
        self.acceleration = self.default_acc
        self.distance

    def update(self, dt):
        self.velocity += self.acceleration * dt
        self.velocity = max(-self.max_velocity, min(self.velocity, self.max_velocity))

        self.position += self.velocity * dt
        if self.position > self.lap:
            self.position = self.position - self.lap

    def react(self, dt):
        v = random()

        if(v>self.randomization):
            self.acceleration = self.default_acc
        else:
            self.acceleration = 0

        

