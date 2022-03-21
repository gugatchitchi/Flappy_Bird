import pygame

# Window Variables
window_width = 600
window_height = 500
framepersecond = 30
title = 'Flappy Bird Game !'

# set height and width of window
window = pygame.display.set_mode((window_width, window_height))

# FPS
framepersecond_clock = pygame.time.Clock()

# Where the ground starts
ground = 0

# Where the sea should be placed on the screen
# It will take bottom 20% of the screen
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
    # 'flappybird': pygame.transform.scale(pygame.image.load('images/bird.png').convert_alpha(), (70,50)),
    'flappybird': pygame.image.load('images/bird.png').convert_alpha(),
    'sea_level': pygame.image.load('images/base.jfif').convert_alpha(),
    'background': pygame.image.load('images/background.jpg').convert_alpha(),
    'pipeimage': (
        pygame.transform.rotate(pygame.image.load('images/pipe.png').convert_alpha(), 180),
        pygame.image.load('images/pipe.png').convert_alpha())
}


# =============================================================================
# This sections describes information about the bird:
# =============================================================================
# Set birds placement
bird_initial_X = int(window_width/5)
bird_initial_Y = int(window_width/2)

# How much gravity affects bird in each iteration/frame
gravity_velocity_change = 1

# What is the speed limit of the birds for each direction
bird_max_velocity = 20
bird_min_velocity = -8

# Birds width and height retrieved from the image
bird_width = game_images['flappybird'].get_width()
bird_height = game_images['flappybird'].get_height()


# =============================================================================
# This sections describes information about the pipes:
# =============================================================================
# Set the vertical gap size between pipes
pipe_gap = 100

# Where this gap can be on the screen
# We set offset of 100px from upper and lower bounds
offset = 100
pipe_gap_y_min = offset
pipe_gap_y_max = elevation - pipe_gap - offset

# Lower and upper bounds for distances between pipes
min_distance_between_pipes = 200
max_distance_between_pipes = 250

# How much gravity affects bird in each iteration/frame
pipe_velocity = 5

# pipe width retrieved from the image
pipe_width = game_images['pipeimage'][0].get_width()




