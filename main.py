import pygame
import constants as const
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

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

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    player = Player(x=const.SCREEN_WIDTH/2, y=const.SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()

    while True:
        screen.fill("black")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.colide_with(player):
                print("Game over!")
                return
        for entity in drawable:
            entity.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1_000

if __name__ == "__main__":
    main()
