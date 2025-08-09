from circleshape import CircleShape
import constants as const
import pygame
from shot import Shot

class Player(CircleShape):

    def __init__(self, x, y):
        super().__init__(x, y, const.PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0.0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
       pygame.draw.polygon(
           surface=screen,
           color="white",
           points=self.triangle(),
           width=2
       )

    def rotate(self, dt):
        self.rotation += const.PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * const.PLAYER_SPEED * dt

    def shot(self):
        shot = Shot(self.position.x, self.position.y)
        velocity = pygame.Vector2(0, 1)
        velocity = velocity.rotate(self.rotation)
        velocity *= const.PLAYER_SHOT_SPEED
        shot.velocity = velocity

    def update(self, dt):
        keys = pygame.key.get_pressed()

        # rotation
        if keys[pygame.K_a]:
            self.rotate(dt)
        if keys[pygame.K_d]:
            self.rotate(-dt)

        # movement
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)

        # shooting
        if keys[pygame.K_SPACE]:
            self.timer -= dt
            if self.timer <= 0:
                self.shot()
                self.timer = const.PLAYER_SHOOT_COOLDOWN
