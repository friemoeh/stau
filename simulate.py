import os
import pygame
import math
from math import sin, radians, degrees, copysign
from pygame.math import Vector2


class Car:
    def __init__(self, x, lap, max_acceleration=5.0):
        self.position = x
        self.lap = lap
        self.velocity = 0.0
        self.max_acceleration = max_acceleration
        self.max_velocity = 20
        self.brake_deceleration = 10
        self.free_deceleration = 2
        
        self.acceleration = 0.0
        self.steering = 0.0

    def update(self, dt):
        self.velocity += self.acceleration * dt
        self.velocity = max(-self.max_velocity, min(self.velocity, self.max_velocity))

        self.position += self.velocity * dt
        if self.position > self.lap:
            self.position = self.position - self.lap
        
       

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

    def run(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(current_dir, "car.png")
        car_image = pygame.image.load(image_path)
        car = Car (0, self.lap)
      #  car = Car (0)
        ppu = 32

        while not self.exit:
            dt = self.clock.get_time() / 1000

            # Event queue
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit = True

            # User input
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
            car.acceleration = max(-car.max_acceleration, min(car.acceleration, car.max_acceleration))

    

            # Logic
            car.update(dt)

            # Drawing


            pos = car.position



            alpha = pos * 2 * math.pi / self.lap

            print(alpha)

            x = math.sin(alpha) * self.radius
            y = math.cos(alpha) * self.radius

            x = x + 12
            y = y + 12

            alpha_deg = alpha * 360 / (2 * math.pi)

            self.screen.fill((0, 0, 0))
            rotated = pygame.transform.rotate(car_image, alpha_deg)
            rect = rotated.get_rect()

            screenPosition = Vector2(x,y)
            self.screen.blit(rotated, screenPosition * ppu - (rect.width / 2, rect.height / 2))
            pygame.display.flip()
        

            self.clock.tick(self.ticks)
        pygame.quit()



if __name__ == '__main__':
    game = Game()
    game.run()
