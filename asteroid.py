import pygame
from circleshape import CircleShape


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
