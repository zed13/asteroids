import pygame
import constants as const
from player import Player

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {const.SCREEN_WIDTH}")
    print(f"Screen height: {const.SCREEN_HEIGHT}")
    print(f"Asteroid min radius: {const.ASTEROID_MIN_RADIUS}")
    print(f"Asteroid kinds: {const.ASTEROID_KINDS}")
    print(f"Asteroid spawn rate: {const.ASTEROID_SPAWN_RATE}")
    print(f"Asteroid max radius: {const.ASTEROID_MAX_RADIUS}")
    pygame.init()
    screen = pygame.display.set_mode((const.SCREEN_WIDTH, const.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(x=const.SCREEN_WIDTH/2, y=const.SCREEN_HEIGHT/2)
    while True:
        screen.fill("black")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        player.update(dt)
        player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1_000

if __name__ == "__main__":
    main()
