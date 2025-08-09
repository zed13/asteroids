from circleshape import CircleShape
import constants as const
import pygame


class Shot(CircleShape):

    def __init__(self, x, y):
        super().__init__(x, y, const.SHOT_RADIUS)


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
