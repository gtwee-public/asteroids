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
        # shot cooldown timer
        self.time_since_last_shot += dt

        # movement logic
        if keys[pygame.K_a]: # rotate right
            self.rotate(dt, direction=-1)
        if keys[pygame.K_d]: # rotate left
            self.rotate(dt, direction=1)
        if keys[pygame.K_w]: # move forward
            self.move(dt, direction=1)
        if keys[pygame.K_s]: # move backwards
            self.move(dt, direction=-1)
        if keys[pygame.K_SPACE]: # shoot shot
            self.shoot(dt)
        # --- Apply velocity to position ---
        self.position += self.velocity * dt
        # --- Apply friction to slow down gradually ---
        self.velocity *= 0.99  # tweak this for more/less drift

        # --- Keep player within screen bounds ---
        min_x = SCREEN_GAP
        max_x = SCREEN_WIDTH - SCREEN_GAP
        min_y = SCREEN_GAP
        max_y = SCREEN_HEIGHT - SCREEN_GAP

        # --- Soft collision with screen boundaries ---
        if self.position.x < min_x:
            self.position.x = min_x  # snap back inside bounds
            self.velocity.x = abs(self.velocity.x) * 0.5  # bounce right
        elif self.position.x > max_x:
            self.position.x = max_x
            self.velocity.x = -abs(self.velocity.x) * 0.5  # bounce left

        if self.position.y < min_y:
            self.position.y = min_y
            self.velocity.y = abs(self.velocity.y) * 0.5  # bounce down
        elif self.position.y > max_y:
            self.position.y = max_y
            self.velocity.y = -abs(self.velocity.y) * 0.5  # bounce up

        # --- Update and remove off-screen shots ---
        for shot in self.shots[:]:  # iterate over a copy to safely remove
            shot.update(dt)
            if shot.is_off_screen():
                self.shots.remove(shot)

    def rotate(self, dt, direction):
        self.rotation += (PLAYER_TURN_SPEED * dt * direction)

    def move(self, dt, direction):
        forward = (pygame.Vector2(0, 1).rotate(self.rotation) * direction)
        self.velocity += forward * PLAYER_ACCELERATION * dt
        
        if self.velocity.length() > PLAYER_MAX_SPEED:
            self.velocity.scale_to_length(PLAYER_MAX_SPEED)

    def shoot(self, dt):
        if self.time_since_last_shot >= SHOT_COOLDOWN:
            forward = pygame.Vector2(0, 1).rotate(self.rotation)
            velocity = forward * PLAYER_SHOT_SPEED
            shot = Shot(self.position.x, self.position.y, SHOT_RADIUS, velocity)
            self.shots.append(shot)
            self.time_since_last_shot = 0


