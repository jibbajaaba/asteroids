import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    # function to create a triangle but with a round hit box
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    # function to create player ship
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), width=2)

    # function to update player rotation
    def update(self, dt):
        keys = pygame.key.get_pressed()

        # press a with negative delta time to get left rotation
        if keys[pygame.K_a]:
            self.rotate(-dt)
        # positive delta time for right rotation
        if keys[pygame.K_d]:
            self.rotate(dt)

    def rotate(self, dt):
        # add player turn speed and delta time to get rotation
        self.rotation += PLAYER_TURN_SPEED * dt
