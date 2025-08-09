import pygame
from circleshape import CircleShape
import constants as const
import random
from ctypes.wintypes import POINT

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
       pygame.draw.circle(
           surface=screen,
           color="white",
           center=self.position,
           width=2,
           radius=self.radius,
       )

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius == const.ASTEROID_MIN_RADIUS:
            return
        split_angle = random.uniform(20, 50)
        fst_velocity = self.velocity.rotate(split_angle)
        snd_velocity = self.velocity.rotate(-split_angle)
        new_radius = self.radius - const.ASTEROID_MIN_RADIUS
        (x, y) = self.position
        fst_asteroid = Asteroid(x, y, new_radius)
        snd_asteroid = Asteroid(x, y, new_radius)
        fst_asteroid.velocity = fst_velocity * 1.2
        snd_asteroid.velocity = snd_velocity * 1.2
