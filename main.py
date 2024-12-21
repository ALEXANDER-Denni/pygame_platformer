import pygame
import os

import collision
import player
import platforms
import moving_platform
import laser
import spikes

os.environ['SDL_AUDIODRIVER'] = 'directx'

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pygame Platformer")

FPS = 60
clock = pygame.time.Clock()


player_object = player.player(500, 100, 10, 20, screen)

move_left = False
move_right = False
move_up = False
move_down = False
jump = False
shoot = False

def draw_background():
    screen.fill((0, 255, 0))

level_platforms = pygame.sprite.Group()

level_platforms.add(platforms.platform(50, 200, 500, 100, screen))
level_platforms.add(platforms.platform(200, 100, 100, 10, screen))

player_bullets = pygame.sprite.Group()
lasers = pygame.sprite.Group()
lasers.add(laser.laser(100, 100, 0, 1, screen))

moving_platform_1 = moving_platform.moving_platform(40, 180, 60, 5, SCREEN_WIDTH, 5*60, screen)
level_platforms.add(moving_platform_1)

spike = spikes.spike(200, 500, 200, 10, 1, screen)#delete

run = True
while run:
    draw_background()
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                move_left = True
            if event.key == pygame.K_d:
                move_right = True
            if event.key == pygame.K_w:
                jump = True
            if event.key == pygame.K_s:
                move_down = True
            if event.key == pygame.K_SPACE:
                shoot = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                move_left = False
            if event.key == pygame.K_d:
                move_right = False
            if event.key == pygame.K_w:
                jump = False
            if event.key == pygame.K_s:
                move_down = False
            if event.key == pygame.K_SPACE:
                shoot = False

    level_platforms.update()
    moving_platform_1.update()
    lasers.update()
    player_object.move(move_left, move_right, jump, move_down, level_platforms)
    if shoot:
        player_object.shoot(player_bullets)
    collision.player_damage_collisions(player_object, player_bullets, lasers) # replace player_bullets with enemy_bullets once enemies are added
    player_bullets.update()
    player_object.draw()
    spike.draw() # delete
    pygame.display.update()  


#add spike group, comment code, add invincibility frames, add switches and doors, add enemies, add images, add level builder script