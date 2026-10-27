import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event

class Asteroid(CircleShape):

    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20, 50)
            asteroid1_vec = self.velocity.rotate(angle)
            asteroid2_vec = self.velocity.rotate(-angle)
            radius2 = self.radius - ASTEROID_MIN_RADIUS
            Asteroid(self.position.x, self.position.y, radius2).velocity = asteroid1_vec * 1.2
            Asteroid(self.position.x, self.position.y, radius2).velocity = asteroid2_vec * 1.2