import pygame
from constants import *
from circleshape import CircleShape
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_cooldown = 0


    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]


    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            Player.rotate(self, dt * -1)
        if keys[pygame.K_d]:
            Player.rotate(self, dt)
        if keys[pygame.K_w]:
            Player.move(self, dt)
        if keys[pygame.K_s]:
            Player.move(self, dt * -1)
        if keys[pygame.K_SPACE]:
            Player.shoot(self)
            self.shoot_cooldown -= dt


    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), width=2)


    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt


    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def shoot(self):
        if self.shoot_cooldown > 0:
            return
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1)
        shot.velocity = shot.velocity.rotate(self.rotation)
        pygame.math.Vector2.scale_to_length(shot.velocity, PLAYER_SHOOT_SPEED)
        self.shoot_cooldown = PLAYER_SHOOT_COOLDOWN
