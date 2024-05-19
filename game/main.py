import pygame
import random
from sys import exit

pygame.init()

pygame.display.set_caption('Test reaction speed')

clock = pygame.time.Clock()

def main():
    game = random.randint(1, 5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                points += capture_fish()
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()


if __name__ == '__main__':
    main()