# this allows us to use code from the open-source pygame library throughout this file
import pygame
import sys

# pyright: reportUndefinedVariable=false
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import *
from shot import Shot
from ui_helpers import render_screen, draw_lives, reset

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    pygame.init()
    py_clock = pygame.time.Clock()
    dt = 0
    hit_time = 0

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
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    rock_field = AsteroidField()

    gamestate = "start"

    while True:
        if gamestate == "start":
            screen.fill((0,0,0))
            render_screen(screen, "Asteroids!", "Press ANY key to start", "red", "white")

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN:
                    gamestate = "playing"            

        elif gamestate == "playing":
            print("Playing")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        gamestate = "paused"
                    continue

            if pygame.time.get_ticks() - hit_time > INVULNERABILITY_TIME:
                player.is_invulnerable = False

            for p in updatable:
                p.update(dt)

            for asteroid in asteroids:
                if asteroid.collision_check(player):
                    print("Game over!")
                    if not player.is_invulnerable:
                        player.lives -= 1
                        asteroid.kill()
                        player.is_invulnerable = True
                        hit_time = pygame.time.get_ticks()

                    if player.lives <= 0:
                        gamestate = "game over"
                    else: 
                        print (f"Lives remaining: {player.lives}")
                        #implement invulnerability so lives dont dissapear instantly

                for bullet in shots:
                    if asteroid.collision_check(bullet):
                        bullet.kill()
                        asteroid.split()

            screen.fill("black")

            for p in drawable:
                if player.is_invulnerable == True:
                    if p == player and pygame.time.get_ticks() % 2 == 0:                
                        continue
                p.draw(screen)

            draw_lives(screen, player)

            pygame.display.flip()            

        elif gamestate == "paused":
            print("Paused")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        gamestate = "playing"
                             
            screen.fill("black")
            render_screen(screen, "Paused", "Press Escape to resume", "red", "yellow")

        elif gamestate == "game over":
            print("Game over")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.QUIT
                        return
                    if event.key == pygame.K_r:
                        #RESET CALL HERE
                        reset(screen, player, rock_field, asteroids, updatable, drawable)
                        gamestate = "playing"
                        
            render_screen(screen, "Game Over", "Press R to restart or Q to quit", "dark red", "white")

        # limit framerate to 60 FPS
        dt = py_clock.tick(60) / 1000

if __name__ == "__main__":
    main()
