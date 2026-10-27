import pygame
import sys

from logger import log_event

from player import Player
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from asteroid import Asteroid
from asteroid_field import AsteroidField

def main():
    print(f"Starting Asteroids with pygame version {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    player = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)
    AsteroidField()



    # Game loop
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        dt = clock.tick(60)/1000
        updatable.update(dt)

        for d in drawable:
            d.draw(screen)
        pygame.display.flip()

        for a in asteroids:
            is_collision = player.collides_with(a)
            if is_collision:
                log_event("player_hit")
                print("Game over!")
                sys.exit()

if __name__ == "__main__":
    main()
