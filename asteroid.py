import pygame
import random

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
#        print(f"{self.radius} vs {ASTEROID_MIN_RADIUS}")
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        SPLIT_SPEED = 1.2
        split_angle = random.uniform(20, 50)

        rotate_1 = self.velocity.rotate(split_angle)
        rotate_2 = self.velocity.rotate(-split_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        Asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        Asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius) 

        Asteroid_1.velocity = rotate_1 * SPLIT_SPEED
        Asteroid_2.velocity = rotate_2 * SPLIT_SPEED
        
