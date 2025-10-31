# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player

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

    # create groups
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()

    # set player group containers
    Player.containers = (updatables, drawables)
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    

    # main game loop
    game_running = True
    while game_running:
        # It will pause the game loop until 1/60th of a 
        # second has passed
        dt = (clock.tick(60) / 1000)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_running = False

        # --- Fill the screen with black ---
        screen.fill((0, 0, 0))

        #player.update(dt)
        #player.draw(screen)

        # --- Update and Draw items on screen ---
        updatables.update(dt)
        for x in drawables:
            x.draw(screen)        

        # --- Update the display ---
        pygame.display.flip()



    pygame.quit()
            


if __name__ == "__main__":
    main()
