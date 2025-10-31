import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shots = []
        self.time_since_last_shot = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)


    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.time_since_last_shot += dt

        if keys[pygame.K_a]:
            self.rotate(dt, direction=-1)

        if keys[pygame.K_d]:
            self.rotate(dt, direction=1)

        if keys[pygame.K_w]:
            self.move(dt, direction=1)

        if keys[pygame.K_s]:
            self.move(dt, direction=-1)

        if keys[pygame.K_SPACE]:
            self.shoot(dt)

        for shot in self.shots:
            shot.update(dt)

        # --- Update and remove off-screen shots ---
        for shot in self.shots[:]:  # iterate over a copy to safely remove
            shot.update(dt)
            if shot.is_off_screen():
                self.shots.remove(shot)

    def rotate(self, dt, direction):
        self.rotation += (PLAYER_TURN_SPEED * dt * direction)

    def move(self, dt, direction):
        forward = (pygame.Vector2(0, 1).rotate(self.rotation) * direction)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self, dt):
        if self.time_since_last_shot >= SHOT_COOLDOWN:
            forward = pygame.Vector2(0, 1).rotate(self.rotation)
            velocity = forward * PLAYER_SHOT_SPEED
            shot = Shot(self.position.x, self.position.y, SHOT_RADIUS, velocity)
            self.shots.append(shot)
            self.time_since_last_shot = 0

