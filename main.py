import pygame
from constants import *

def main():
    # Initialize pygame
    pygame.init()
    # set game screen height and width
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # create clock object and save to variable
    clock = pygame.time.Clock()
    # dt = delta time
    dt = 0

    # Game loop
    while True:
        # allows player to exit out of game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # creates black background
        screen.fill("black")
        pygame.display.flip()
        # set clock object to 60 milliseconds and divide by 1000 to convert to seconds
        # save to dt
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
