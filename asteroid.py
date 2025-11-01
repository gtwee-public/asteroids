import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        # Remove the current asteroid
        self.kill()
        
        # Stop if it's already the smallest size
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        # Get a random spread angle between 20° and 50°
        random_angle = random.uniform(20, 50)

        # Base direction is the asteroid's current velocity direction
        base_direction = self.velocity.normalize()
        
        # Rotate the base direction to create two new velocity vectors
        velocity1 = base_direction.rotate(random_angle)
        velocity2 = base_direction.rotate(-random_angle)

        # Reduce the radius for the new asteroids
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Create the new asteroids
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

        # Apply velocity scaled by the parent's speed (slightly faster)
        speed = self.velocity.length() * 1.2
        asteroid1.velocity = velocity1 * speed
        asteroid2.velocity = velocity2 * speed






