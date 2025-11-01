import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from star import Star
from starfield import StarField

def main():
    # initialize pygame
    pygame.init()

    clock = pygame.time.Clock()
    dt = 0

    # print console message
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    print("===========================================")

    # use pygame's display.set_mode() to get a new GUI window:
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # create groups
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    stars = pygame.sprite.Group()

    # set group containers
    Player.containers = (updatables, drawables)
    Asteroid.containers = (updatables, drawables, asteroids)
    AsteroidField.containers = (updatables)
    Shot.containers = (updatables, drawables, shots)
    Star.containers = (updatables, drawables, stars)
    StarField.containers = (updatables)

    # spawn player
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    
    asteroid_field = AsteroidField()
    star_field = StarField()

    # main game loop
    game_running = True
    score = 0
    health = 3
    while game_running:
        # It will pause the game loop until 1/60th of a 
        # second has passed
        dt = (clock.tick(60) / 1000)

        # logic to exit game by user
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_running = False

        # --- Fill the screen with black ---
        screen.fill((0, 0, 0))

        # --- Update and Draw items on screen ---
        updatables.update(dt)
        for x in drawables:
            x.draw(screen)        

        # --- Update the display ---
        pygame.display.flip()

        # check for asteroid collisions
        for a in asteroids:
            # check for player collision with asteroid
            if a.collision_detection(player):
                if health <= 1:
                    print("Game over!")
                    game_running = False
                else:
                    health -= 1
                    a.kill()
                    print(f"{health} health remaining")

            # check for shot collision with asteroid
            for b in shots:
                if a.collision_detection(b):
                    b.kill()
                    a.split()
                    score += 5
                    print(f"Score: {score}")
                    
        



    pygame.quit()
            


if __name__ == "__main__":
    main()
