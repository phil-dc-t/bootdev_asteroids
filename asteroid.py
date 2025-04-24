import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            rand_angle = random.uniform(20,50)
            asteroid_1 = Asteroid(self.position.x, self.position.y, self.radius-ASTEROID_MIN_RADIUS)
            asteroid_2 = Asteroid(self.position.x, self.position.y, self.radius-ASTEROID_MIN_RADIUS)
            asteroid_1.velocity = pygame.Vector2.rotate(self.velocity, rand_angle)*1.2
            asteroid_2.velocity = pygame.Vector2.rotate(self.velocity, -rand_angle)*1.2

    def draw(self, screen):
        return pygame.draw.circle(screen, pygame.Color("white"), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt