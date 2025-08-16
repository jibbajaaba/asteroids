import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


# Astroid class
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    # draws the asteroids
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    # updates speed and direction in a straight line
    def update(self, dt):
        self.position += self.velocity * dt

    # asteroid split logic
    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        rand_angle = random.uniform(20, 50)
        vector_pos = self.velocity.rotate(rand_angle)
        vector_neg = self.velocity.rotate(-rand_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        astroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        astroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        astroid_1.velocity = vector_pos * 1.2
        astroid_2.velocity = vector_neg * 1.2
