import pygame
import os

import collision
import bullet

START_HEALTH = 100
MAX_HEALTH = 100
PLAYER_WIDTH = 100
PLAYER_HEIGHT = 100
STARTER_AMMO = 100
FIRE_DELAY = 100
BULLET_DAMAGE = 100
RELOAD_TIME = 2000
ACCELERATION = 1
FRICTION = 3
GRAVITY = 1
SPEED = 10
JUMP_FORCE = 100
DOUBLE_JUMP_DELAY = 110

class player(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, screen):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([w,h])
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction = 1
        self.screen = screen

        self.x_velocity = 0
        self.y_velocity = 0
        self.accel = ACCELERATION
        self.max_speed = SPEED

        self.in_air = False
        self.double_jump = False
        self.jump_time = 0

        self.health = START_HEALTH

        self.ammo = STARTER_AMMO
        self.fire_time = 0
        self.time_of_reload = 0
        self.reloading = False

    def move(self, left, right, up, down, platforms):
        self.reload() # add to update script in future
        x_v = 0
        y_v = 0

        if right and not self.in_air:
            x_v += self.accel
        if left and not self.in_air:
            x_v -= self.accel
        if down:
            y_v += self.accel
        """if up: use for flying
            y_v -=self.accel"""
        if up:
            if not self.in_air:
                y_v = -JUMP_FORCE
                self.double_jump = True
                self.jump_time = pygame.time.get_ticks()
            elif self.double_jump and pygame.time.get_ticks() - self.jump_time > DOUBLE_JUMP_DELAY:
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
                if abs(self.x_velocity) < FRICTION:
                    self.x_velocity = 0
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
        max_moves = collision.platform_collisions(self, platforms)
        if abs(max_moves[0]) < abs(self.x_velocity):
            self.x_velocity = max_moves[0]
            self.rect.x += self.x_velocity
            self.x_velocity = 0
        if abs(max_moves[1]) < abs(self.y_velocity):
            if self.y_velocity <= 0:
                self.in_air = False
            self.y_velocity = max_moves[1]
            self.rect.y += self.y_velocity
            self.y_velocity = 0
        self.in_air = not max_moves[2]
        self.rect.x += self.x_velocity
        self.rect.y += self.y_velocity

    def shoot(self, bullet_list):
        if pygame.time.get_ticks()-self.fire_time > FIRE_DELAY:
            if self.ammo > 0:
                self.fire_time = pygame.time.get_ticks()
                bullet_list.add(bullet.bullet(self.rect.x, self.rect.y, 100, self.direction, True, self.screen))
                self.ammo -= 1
                if self.ammo == 0:
                    self.time_of_reload = pygame.time.get_ticks()
                    self.reloading = True
                
    def reload(self):  
        if self.reloading and pygame.time.get_ticks() - self.time_of_reload > RELOAD_TIME:
            self.ammo = STARTER_AMMO
            self.reloading = False

    def push(self, amount):
        self.rect.x += amount

        
    def draw(self):
        self.screen.blit(pygame.transform.flip(self.image, self.direction==1, False), self.rect)
