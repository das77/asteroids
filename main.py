# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from player_shot import Shot
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # sets the screen size
    clock = pygame.time.Clock() # refreshes the screen
    dt = 0  # 
    plyer = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) # init the Player class
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    updatable.add(plyer)
    drawable.add(plyer)
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    AsteroidField()
    Shot.containers = (shots, updatable, drawable)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for updates in updatable:
            updates.update(dt)            
        
        for objects in asteroids:
            if plyer.collisions(objects):
                print("Game over!")
                sys.exit()
            for shot in shots:
                if objects.collisions(shot):
                    shot.kill()
                    result = objects.split()
                    if result:
                        ast1, ast2 = result
                    asteroids.add(ast1, ast2)
                    updatable.add(ast1, ast2)

        screen.fill(color="#000000")
        
        for obj in drawable:
            obj.draw(screen)
        
        pygame.display.flip()

        dt = clock.tick(60) /1000 # display update limited to 60 FPS

if __name__ == "__main__":
    main()