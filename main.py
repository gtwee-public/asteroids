# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

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
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # set group containers
    Player.containers = (updatables, drawables)
    Asteroid.containers = (updatables, drawables, asteroids)
    AsteroidField.containers = (updatables)
    Shot.containers = (updatables, drawables, shots)

    # spawn player
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    
    asteroid_field = AsteroidField()

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

        # check for player collision with asteroid
        for a in asteroids:
            if a.collision_detection(player):
                print("Game over!")
                game_running = False

            for b in shots:
                if a.collision_detection(b):
                    b.kill()
                    a.split()
                    
        



    pygame.quit()
            


if __name__ == "__main__":
    main()
