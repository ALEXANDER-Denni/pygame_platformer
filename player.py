import pygame
import os

START_HEALTH = 100
MAX_HEALTH = 100
FIRE_RATE = 100
BULLET_DAMAGE = 100
PLAYER_WIDTH = 100
PLAYER_HEIGHT = 100
STARTER_AMMO = 100
ACCELERATION = 1
FRICTION = 1
GRAVITY = 1
SPEED = 10
JUMP_FORCE = 100
DOUBLE_JUMP_DELAY = 110

class player:
    def __init__(self, x, y, w, h):
        self.rect = pygame.Rect(x, y, w,h)
        self.x_velocity = 0
        self.y_velocity = 0
        self.accel = ACCELERATION
        self.max_speed = SPEED

        self.in_air = False
        self.double_jump = False
        self.jumpTime = 0

        self.health = START_HEALTH
        self.ammo = STARTER_AMMO
        

    def move(self, left, right, up, down):
        x_v = 0
        y_v = 0

        if right:
            if self.x_velocity < 0 and not right:
                x_v+=self.x_velocity
            x_v += self.accel
        if left:
            if self.x_velocity > 0 and not left:
                x_v+=self.x_velocity
            x_v -= self.accel
        if down:
            y_v += self.accel
        if up:
            if not self.in_air:
                y_v = -JUMP_FORCE
                self.double_jump = True
                self.jumpTime = pygame.time.get_ticks()
            elif self.double_jump and pygame.time.get_ticks() - self.jumpTime > DOUBLE_JUMP_DELAY:
                y_v = -JUMP_FORCE
                self.double_jump = False
            self.in_air = True
        if self.in_air:
            y_v += GRAVITY
            if down:
                y_v += self.accel
        else:
            self.y_velocity = 0
            if not right and not left:
                if self.x_velocity > 0:
                    x_v -= FRICTION
                if self.x_velocity < 0:
                    x_v += FRICTION
        self.x_velocity += x_v
        self.y_velocity += y_v

        if self.x_velocity > self.max_speed:
            self.x_velocity = self.max_speed
        elif self.x_velocity < -self.max_speed:
            self.x_velocity = -self.max_speed
        if self.y_velocity > self.max_speed:
            self.y_velocity = self.max_speed
        elif self.y_velocity < -self.max_speed:
            self.y_velocity = -self.max_speed

        self.rect.x += self.x_velocity
        self.rect.y += self.y_velocity

    def draw(self, screen,):
        pygame.draw.rect(screen, (0, 0, 255), self.rect)
