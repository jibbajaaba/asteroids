import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS


# shot class to handle all shooting objects
class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    # draw the shot on the screen
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, SHOT_RADIUS, 2)

    # update shot position based on velocity and delta time
    def update(self, dt):
        self.position += self.velocity * dt
