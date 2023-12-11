import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Valdymas su W, A, S, D')

player_x, player_y = 200, 150
player_speed = 0.03


running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[K_w]:
        player_y -= player_speed
    if keys[K_s]:
        player_y += player_speed
    if keys[K_a]:
        player_x -= player_speed
    if keys[K_d]:
        player_x += player_speed

    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0, 0, 255), (player_x, player_y, 50, 50))
    pygame.display.update()

pygame.quit()
