import pygame
import os

import collision
import player

os.environ['SDL_AUDIODRIVER'] = 'directx'

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pygame Platformer")

FPS = 60
clock = pygame.time.Clock()


player_object = player.player(100, 100, 10, 20)

move_left = False
move_right = False
move_up = False
move_down = False
jump = False


def draw_background():
    screen.fill((0, 255, 0))

class TEMP:
    def __init__(self,x,y,w,h):
        self.rect = pygame.Rect(x,y,w,h)

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
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                move_left = False
            if event.key == pygame.K_d:
                move_right = False
            if event.key == pygame.K_w:
                jump = False
            if event.key == pygame.K_s:
                move_down = False
    
    pygame.draw.rect(screen, (0, 0, 0), TEMP(50,200,500,100))
    pygame.draw.rect(screen, (0, 0, 0), TEMP(200, 180, 100, 20))
    player_object.move(move_left, move_right, jump, move_down)
    collide = collision.platform_collisions(player_object, [TEMP(50,200,500,100), TEMP(200, 180, 100, 20)])# return (X collision, Y collision)
    if collide[0]:
        player_object.x_velocity = 0
    if collide[1]:
        player_object.in_air = False
    else:
        player_object.in_air = True
    player_object.draw(screen)
    
    pygame.display.update()

#add bullets, add enemies, add more platforms, add moving platforms, add lasers, add switches and doors, add level builder script