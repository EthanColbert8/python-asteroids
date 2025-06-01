import pygame
from constants import * # this is a small project, so just make importing constants easy
from player import Player, Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0.0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable) # sets the containers at the class level
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    Shot.containers = (shots, updatable, drawable)

    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill((0, 0, 0)) # RGB black

        updatable.update(dt)
        
        for ast in asteroids:
            for shot in shots:
                if ast.colliding(shot):
                    ast.kill()
                    shot.kill()

        # drawable.draw(screen) # this crashes because we don't have images for the sprites
        for to_draw in drawable:
            to_draw.draw(screen)
        
        for ast in asteroids:
            if ast.colliding(player):
                print("Game over!")
                return


        pygame.display.flip()
        dt = clock.tick(60) / 1000.0

if (__name__ == "__main__"):
    main()