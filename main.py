# this allows us to use code from the open-source pygame library throughout this file
import pygame

# pyright: reportUndefinedVariable=false
from constants import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    pygame.init()
    py_clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
#        pygame.Surface.fill(screen, (0,0,0)) - works, was my solution, swapping 
        screen.fill("black")
        pygame.display.flip()

        # limit framerate to 60 FPS
        dt = py_clock.tick(60) / 1000

if __name__ == "__main__":
    main()
