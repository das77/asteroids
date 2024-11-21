from circleshape import CircleShape
from constants import *
import pygame

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, radius=SHOT_RADIUS)

    def draw(self, surface):
        pygame.draw.circle(surface, color="white", center=self.position, radius=self.radius, width=1)

    def update(self, dt):
        self.position += self.velocity * dt