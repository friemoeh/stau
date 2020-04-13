from random import random

class Car:
    def __init__(self, x, lap, startvelocity):
        self.position = x
        self.lap = lap
        self.default_acc=3
        self.velocity = startvelocity
        self.probDeacc = 0.3
        self.max_velocity = 20
        self.acceleration = 0
        self.distance = 0
        self.minDist = self.lap / 200
    

    def update(self, dt):
        self.velocity += self.acceleration * dt
        self.velocity = max(0, min(self.velocity, self.max_velocity))

        self.position += self.velocity * dt
        if self.position > self.lap:
            self.position = self.position - self.lap

    def react(self, dt):
        # default: beschleunige
        acc = self.default_acc

        # trödeln in probDeacc Fällen
        reactProb = random()
        if(reactProb < self.probDeacc):
            acc = - self.default_acc

        #s: der zu zurück legende Weg        
        s = self.velocity * dt + acc * dt * dt /2
        # wenn man das Vorausfahrende FAhrzeug überholen würde dann wird abgebremst
        if(s>self.distance- self.minDist):
            self.acceleration = 2 * (self.distance - self.minDist - self.velocity * dt) / (dt * dt)
        else:
            self.acceleration = acc 
