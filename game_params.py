import pygame


# ----------------------------------------
# ALL THE GAME PARAMETERS ARE LISTED HERE
# ----------------------------------------
# Window parameters
WIDTH, HEIGHT = 900, 500
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Birds")
# This is used to limit FPS
FPS = 60
# Background rectangle
BACKGROUND = pygame.Rect(0, 0, WIDTH, HEIGHT)
# Moving parts
PIPE_UP = pygame.Rect(100, 0, 40, 200)
PIPE_DOWN = pygame.Rect(100, 300, 40, 200)