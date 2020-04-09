import os
import pygame
import math
from math import sin, radians, degrees, copysign
from pygame.math import Vector2

from Car import Car


        
   
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

       
        rotated = pygame.transform.rotozoom(car_image, alpha_deg, 0.3)
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

            for i in range (self.numberCars):
                car1 = garage [i]
                if i == self.numberCars - 1:
                    car2 = garage [0]
                    car1.distance =  car2.position - car1.position
                else:
                    car2 = garage [i + 1]
                    car1.distance = car2.position - car1.position

                if car1.distance < 0:
                    car1.distance += self.lap


            self.cleancars()

            for car in garage:
                car.react(dt)
                car.update(dt)
                self.paintcar(car, car_image)

            

            pygame.display.flip()
        
            self.clock.tick(self.ticks)
        pygame.quit()


  
if __name__ == '__main__':
    game = Game()
    game.run()
