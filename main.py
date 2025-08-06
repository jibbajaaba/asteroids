import pygame
from constants import *

def main():
    # Initialize pygame
    pygame.init()
    # set game screen height and width
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Game loop
    while True:
        # allows player to exit out of game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        # creates black background
        screen.fill("black")
        pygame.display.flip()

if __name__ == "__main__":
    main()
