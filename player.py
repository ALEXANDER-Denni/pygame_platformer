import time
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

class player:
    def __init__(self,x,y,w,h):
        self.x= x
        self.y = y
        self.w = w
        self.h = h
        self.x_velocity = 0
        self.y_velocity = 0
        self.accel = ACCELERATION
        self.max_speed = SPEED
        self.health = START_HEALTH
        self.ammo = STARTER_AMMO
        self.in_air = False
    def move(self, left, right, up, down):
        x_v = 0 
        y_v = 0

        if right:
            x_move+=self.accel
        if left:
            x_move-=self.accel
        if up and not in_air:
            # jump
            pass
        if in_air:
            self.y_v+=GRAVITY
            if down:
                y_v+=self.accel

        self.x_velocity += x_v
        self.y_velocity += y_v
        
        if self.x_velocity > self.max_speed:
            self.x_velocity = self.max_speed
        elif self.x_velocity <  -self.max_speed:
            self.x_velocity = -self.max_speed
        if self.y_velocity > self.max_speed:
            self.y_velocity = self.max_speed
        elif self.y_velocity <  -self.max_speed:
            self.y_velocity = -self.max_speed
        
