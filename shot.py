import pygame
from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y, radius, velocity):
        super().__init__(x, y, radius)
        self.velocity = velocity

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def is_off_screen(self):
        """Return True if the shot is outside the screen bounds."""
        return (
            self.position.x < 0 or
            self.position.x > SCREEN_WIDTH or
            self.position.y < 0 or
            self.position.y > SCREEN_HEIGHT
        )
