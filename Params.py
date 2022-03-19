import pygame

# Window Variables
window_width = 600
window_height = 499
framepersecond = 32
title = 'Flappy Bird Game !'

# set height and width of window
window = pygame.display.set_mode((window_width, window_height))

# Set birds placement
horizontal = int(window_width/5)
vertical = int(window_width/2)

# Where the ground starts
ground = 0

# Elevation of the bird after key is pressed
elevation = window_height * 0.8

# Game Images
game_images = {
    'scoreimages': (
        pygame.image.load('images/0.png').convert_alpha(),
        pygame.image.load('images/1.png').convert_alpha(),
        pygame.image.load('images/2.png').convert_alpha(),
        pygame.image.load('images/3.png').convert_alpha(),
        pygame.image.load('images/4.png').convert_alpha(),
        pygame.image.load('images/5.png').convert_alpha(),
        pygame.image.load('images/6.png').convert_alpha(),
        pygame.image.load('images/7.png').convert_alpha(),
        pygame.image.load('images/8.png').convert_alpha(),
        pygame.image.load('images/9.png').convert_alpha()
    ),
    'flappybird': pygame.image.load('images/bird.png').convert_alpha(),
    'sea_level': pygame.image.load('images/base.jfif').convert_alpha(),
    'background': pygame.image.load('images/background.jpg').convert_alpha(), 'pipeimage': (
        pygame.transform.rotate(pygame.image.load('images/pipe.png').convert_alpha(), 180),
        pygame.image.load('images/pipe.png').convert_alpha())
}

