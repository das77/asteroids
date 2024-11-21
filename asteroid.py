from circleshape import CircleShape
from constants import *
import pygame
import random
from player import Player

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius=radius)
        self.rotate = 0
    
    def draw(self, surface):
        pygame.draw.circle(surface, color="white", center=self.position, radius=self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        if new_radius < ASTEROID_MIN_RADIUS:
            return None
        # current_velocity = self.velocity
        v1 = self.velocity.rotate(random_angle)
        v2 = self.velocity.rotate(-random_angle)
        new_asteroid = Asteroid(self.position, v1, new_radius)
        new_asteroid2 = Asteroid(self.position, v2, new_radius)
        new_asteroid.velocity = v1 * 1.2
        new_asteroid2.velocity = v2 * 1.2
        return new_asteroid, new_asteroid2

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt