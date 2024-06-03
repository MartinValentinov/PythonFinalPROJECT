import pygame
from constants import *
from sys import exit

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Healthy life')
clock = pygame.time.Clock()

sky_surface = pygame.image.load('pictures/Sky.png')
sky_surface = pygame.transform.scale(sky_surface, (WIDTH, HEIGHT - HEIGHT//4.5))
sky_surface_rect = sky_surface.get_rect(topleft = (0, 0))
ground_surface = pygame.image.load('pictures/ground.png')
ground_surface = pygame.transform.scale(ground_surface, (WIDTH, HEIGHT//4.5))
ground_surface_rect = ground_surface.get_rect(topleft = (0, HEIGHT - HEIGHT//4.5))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface, sky_surface_rect)
    screen.blit(ground_surface, ground_surface_rect)

    pygame.display.update()
    clock.tick(60)
