import pygame
from constants import *
from circleshape import CircleShape

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0.0
        self.shot_timer = 0.0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), width=2)
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        # self.position += forward * PLAYER_SPEED * dt
        
        next_velocity = self.velocity + (forward * PLAYER_ACCELERATION * dt)
        
        if (next_velocity.magnitude() > PLAYER_MAX_SPEED):
            self.velocity = forward * PLAYER_MAX_SPEED
        elif (next_velocity.dot(forward) < 0.0):
            self.velocity = pygame.Vector2(0, 0)
        else:
            self.velocity = next_velocity
    
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
        
        self.shot_timer -= dt

        self.position += self.velocity * dt
    
    def shoot(self):
        if self.shot_timer > 0:
            return

        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = forward * PLAYER_SHOT_SPEED
        self.shot_timer = PLAYER_SHOT_COOLDOWN

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, width=2)
    
    def update(self, dt):
        self.position += self.velocity * dt