# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    # initialize pygame
    pygame.init()

    clock = pygame.time.Clock()
    dt = 0


    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # use pygame's display.set_mode() to get a new GUI window:
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    game_running = True
    while game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # --- Fill the screen with black ---
            screen.fill((0, 0, 0))

            # --- Update the display ---
            pygame.display.flip()

            # It will pause the game loop until 1/60th of a 
            # second has passed
            clock.tick(60)
            dt = (clock.get_time() / 1000)
            


if __name__ == "__main__":
    main()
