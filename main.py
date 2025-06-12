# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *


def main():
    pygame.init
    fpsClock = pygame.time.Clock()
    dt = 0
    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)
    pygame.display.set_mode()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\n" "Screen height: {SCREEN_HEIGHT}")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()
        dt = fpsClock.tick(60) / 1000


if __name__ == "__main__":
    main()
