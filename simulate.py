import os
import pygame
import math
from math import sin, radians, degrees, copysign
from pygame.math import Vector2
from random import random
from Car import Car

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

    def update(self, dt):
        self.velocity += self.acceleration * dt
        self.velocity = max(-self.max_velocity, min(self.velocity, self.max_velocity))

        self.position += self.velocity * dt
        if self.position > self.lap:
            self.position = self.position - self.lap

def userReact(car, dt): 
    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_UP]:
        if car.velocity < 0:
            car.acceleration = car.brake_deceleration
        else:
            car.acceleration += 1 * dt
    elif pressed[pygame.K_DOWN]:
        if car.velocity > 0:
            car.acceleration = -car.brake_deceleration
        else:
            car.acceleration -= 1 * dt
    elif pressed[pygame.K_SPACE]:
        if abs(car.velocity) > dt * car.brake_deceleration:
            car.acceleration = -copysign(car.brake_deceleration, car.velocity)
        else:
            car.acceleration = -car.velocity / dt
    else:
        if abs(car.velocity) > dt * car.free_deceleration:
            car.acceleration = -copysign(car.free_deceleration, car.velocity)
        else:
            if dt != 0:
                car.acceleration = -car.velocity / dt
                car.acceleration = max(-car.max_acceleration,
                    min(car.acceleration, car.max_acceleration))

def react(car, dt):
    v = random()

    if(v>car.randomization):
        car.acceleration=car.default_acc
    else:
        car.acceleration=0
        
   
class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Car tutorial")
        width = 720
        height = 720
        self.radius = 8
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.ticks = 60
        self.exit = False
        self.lap = 2 * math.pi * self.radius
        self.numberCars = 10

    def cleancars(self):
        self.screen.fill((0, 0, 0))

    def paintcar(self, car, car_image):
        ppu = 32
        pos = car.position

        alpha = pos * 2 * math.pi / self.lap

        x = math.sin(alpha) * self.radius
        y = math.cos(alpha) * self.radius

        x = x + 12
        y = y + 12

        alpha_deg = alpha * 360 / (2 * math.pi)

       
        rotated = pygame.transform.rotate(car_image, alpha_deg)
        rect = rotated.get_rect()

        screenPosition = Vector2(x,y)
        self.screen.blit(rotated, screenPosition * ppu - (rect.width / 2, rect.height / 2))
    

    def run(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(current_dir, "car.png")
        car_image = pygame.image.load(image_path)
        garage=[]
        for i in range(self.numberCars):
            start = i * self.lap / self.numberCars
            car = Car (start, self.lap, 5)
            garage.append(car)
    
       

        while not self.exit:
            dt = self.clock.get_time() / 1000

            # Event queue
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit = True

            self.cleancars()

            for car in garage:
                react(car, dt)
                car.update(dt)
                self.paintcar(car, car_image)

            
     

            pygame.display.flip()
        
            self.clock.tick(self.ticks)
        pygame.quit()


  
if __name__ == '__main__':
    game = Game()
    game.run()
