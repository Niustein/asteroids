# this allows us to use code from the open-source pygame library throughout this file
import pygame
import sys

# pyright: reportUndefinedVariable=false
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import *
from shot import Shot

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    pygame.init()
    py_clock = pygame.time.Clock()
    dt = 0

    # Creating groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)  
    Shot.containers = (shots, updatable, drawable)
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#    player_init_x = SCREEN_WIDTH / 2
#    player_init_y = SCREEN_HEIGHT / 2
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    rock_field = AsteroidField()

#further testing with boots
#    player2 = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
#    player2.get_position_info()
 
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
#        pygame.Surface.fill(screen, (0,0,0)) - works, was my solution, swapping
        
        for p in updatable:
            p.update(dt) 

#       after competing step and looking at solution: realized I drew this before screen filled        
#        for p in drawable:
#            p.draw(screen)

        for val in asteroids:
            if val.collision_check(player):
                print(f"{val.position} vs {player.position} and the radius are: {val.radius} vs {player.radius}")
                print("Game over!")
                sys.exit(0)
    

        screen.fill("black")

#        player.draw(screen)
        for p in drawable:
            p.draw(screen)

        pygame.display.flip()



        # limit framerate to 60 FPS
        dt = py_clock.tick(60) / 1000

if __name__ == "__main__":
    main()
