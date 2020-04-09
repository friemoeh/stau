from random import random

class Car:
    def __init__(self, x, lap, startvelocity=0, randomization=0.5):
        self.position = x
        self.lap = lap
        self.default_acc=1
        self.velocity = startvelocity
        self.probAcc = 0.4
        self.probDeacc = 0.3
        self.max_acceleration = 5.0
        self.max_velocity = 20
        self.brake_deceleration = 10
        self.free_deceleration = 2
        self.acceleration = self.default_acc
        self.distance = 0
        self.minDist = self.lap / 10

    def update(self, dt):
        self.velocity += self.acceleration * dt
        self.velocity = max(0, min(self.velocity, self.max_velocity))

        self.position += self.velocity * dt
        if self.position > self.lap:
            self.position = self.position - self.lap

    def react(self, dt):
        #beschleunige
        acc = self.default_acc

        #trödeln in probDeacc Fällen
        reactProb = random()
        if(reactProb < self.probDeacc):
            acc = - self.default_acc

        #s: der zu zurück legende Weg        
        s = self.velocity * dt + acc * dt * dt /2
        # wenn man das Vorausfahrende FAhrzeug überholen würde dann wird abgebremst
        if(s>self.distance):
            self.acceleration = 2 * (self.distance - self.velocity * dt) / (dt * dt)
        else:
            self.acceleration = acc 
