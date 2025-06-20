import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, width=2)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        angle = random.uniform(20, 50)

        vel1 = self.velocity.rotate(angle)
        vel2 = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        child1 = Asteroid(self.position.x, self.position.y, new_radius)
        child1.velocity = vel1 * 1.2

        child2 = Asteroid(self.position.x, self.position.y, new_radius)
        child2.velocity = vel2 * 1.2

