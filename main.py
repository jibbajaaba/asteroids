import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    # Initialize pygame
    pygame.init()
    # set game screen height and width
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # create clock object and save to variable
    clock = pygame.time.Clock()
    # dt = delta time
    dt = 0

    # groups which contain elements of the game
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # static containers for player, asteroids and shots
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    # creates the asteroids
    asteroid_field = AsteroidField()

    # creates the player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Game loop
    while True:
        # allows player to exit out of game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # call dt on Player update method to update movement
        updatable.update(dt)
        # creates black background
        screen.fill("black")
        # draws the player on the screen
        for drawables in drawable:
            drawables.draw(screen)

        pygame.display.flip()
        """
        set clock object to 60 milliseconds and divide by 1000 to convert to
        seconds
        """
        # save to dt
        dt = clock.tick(60) / 1000

        for asteroid in asteroids:
            for bullet in shots:
                if not asteroid.collision(bullet):
                    asteroid.kill()
            if not asteroid.collision(player):
                print("Game Over")
                exit()


if __name__ == "__main__":
    main()
