import pygame
from asteroid import Asteroid 

def render_screen(screen, title_text, subtitle_text, title_color, subtitle_color):
    title_style = pygame.font.SysFont("Ariel", 100, True)
    text_style = pygame.font.SysFont("Times New Roman", 50, True)

    title = title_style.render(title_text, True, title_color)
    title_rect = title.get_rect(center = (screen.get_width() / 2, screen.get_height() / 4))
    subtitle = text_style.render(subtitle_text, True, subtitle_color)
    subtitle_rect = subtitle.get_rect(center = (screen.get_width() / 2, screen.get_height() / 2))

    pygame.Surface.blit(screen, title, title_rect)
    pygame.Surface.blit(screen, subtitle, subtitle_rect)

    pygame.display.flip()

def draw_lives(screen, player):
    lives_font = pygame.font.SysFont("Arial", 20)
    lives_text = lives_font.render(f"Lives: {player.lives}", True, "white")
    screen.blit(lives_text, (10, 10))
    pygame.display.flip()

def reset(screen, player, asteroidfield, asteroids_group, updatable_group, drawable_group):
    player.lives = 3
    player.position = pygame.Vector2(screen.get_width() /2, screen.get_height() /2)
    player.is_invulnerable = False

    #clear asteroids and asteroidfield.

    asteroids_group.empty()
    for sprite in updatable_group:
        if isinstance(sprite, Asteroid):
            updatable_group.remove(sprite)
    for sprite in drawable_group:
        if isinstance(sprite, Asteroid):
            drawable_group.remove(sprite)
    
    asteroidfield.spawn_timer = 0