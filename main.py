import time
import pygame
import os
import player

os.environ['SDL_AUDIODRIVER'] = 'directx'

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pygame Platformer")

FPS = 60
clock = pygame.time.Clock()


player_object = player.player(600, 100, 10, 10)

move_left = False
move_right = False


def draw_background():
    screen.fill((0, 255, 0))


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
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                move_left = False
            if event.key == pygame.K_d:
                move_right = False
    player_object.move(move_left, move_right, False, False)
    player_object.draw(screen)
    print(player_object.rect.y)
    pygame.display.update()
