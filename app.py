import sys

import pygame

from object import Ground
from player import Player

WIDTH = 400
HEIGHT = 200
BACKGROUND = pygame.image.load("DMC5Background.png")


def game():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    player = Player(100, 100)
    ground = pygame.sprite.Group()
    for object in range(0, 400, 50):
        ground.add(Ground(object, 200))

    while True:
        screen.blit(BACKGROUND, (0, 0))

        player.update(ground)
        player.draw(screen)
        ground.draw(screen)

        pygame.display.flip()
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


if __name__ == '__main__':
    game()