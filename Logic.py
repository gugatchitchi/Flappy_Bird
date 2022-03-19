import sys
import random
import pygame
from pygame.locals import *
from Params import *

def flappygame(framepersecond_clock):
	your_score = 0
	horizontal = int(window_width/5)
	vertical = int(window_width/2)
	ground = 0
	mytempheight = 100

	# Generating two pipes for blitting on window
	first_pipe = createPipe()
	second_pipe = createPipe()

	# List containing lower pipes
	down_pipes = [
		{'x': window_width+300-mytempheight,
		'y': first_pipe[1]['y']},
		{'x': window_width+300-mytempheight+(window_width/2),
		'y': second_pipe[1]['y']},
	]

	# List Containing upper pipes
	up_pipes = [
		{'x': window_width+300-mytempheight,
		'y': first_pipe[0]['y']},
		{'x': window_width+200-mytempheight+(window_width/2),
		'y': second_pipe[0]['y']},
	]

	# pipe velocity along x
	pipeVelX = -4

	# bird velocity
	bird_velocity_y = -9
	bird_Max_Vel_Y = 10
	bird_Min_Vel_Y = -8
	birdAccY = 1

	bird_flap_velocity = -8
	bird_flapped = False
	while True:
		for event in pygame.event.get():
			if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
				if vertical > 0:
					bird_velocity_y = bird_flap_velocity
					bird_flapped = True

		# This function will return true
		# if the flappybird is crashed
		game_over = isGameOver(horizontal,
							vertical,
							up_pipes,
							down_pipes)
		if game_over:
			return

		# check for your_score
		playerMidPos = horizontal + game_images['flappybird'].get_width()/2
		for pipe in up_pipes:
			pipeMidPos = pipe['x'] + game_images['pipeimage'][0].get_width()/2
			if pipeMidPos <= playerMidPos < pipeMidPos + 4:
				your_score += 1
				print(f"Your your_score is {your_score}")

		if bird_velocity_y < bird_Max_Vel_Y and not bird_flapped:
			bird_velocity_y += birdAccY

		if bird_flapped:
			bird_flapped = False
		playerHeight = game_images['flappybird'].get_height()
		vertical = vertical + \
			min(bird_velocity_y, elevation - vertical - playerHeight)

		# move pipes to the left
		for upperPipe, lowerPipe in zip(up_pipes, down_pipes):
			upperPipe['x'] += pipeVelX
			lowerPipe['x'] += pipeVelX

		# Add a new pipe when the first is
		# about to cross the leftmost part of the screen
		if 0 < up_pipes[0]['x'] < 5:
			newpipe = createPipe()
			up_pipes.append(newpipe[0])
			down_pipes.append(newpipe[1])

		# if the pipe is out of the screen, remove it
		if up_pipes[0]['x'] < -game_images['pipeimage'][0].get_width():
			up_pipes.pop(0)
			down_pipes.pop(0)

		# Lets blit our game images now
		window.blit(game_images['background'], (0, 0))
		for upperPipe, lowerPipe in zip(up_pipes, down_pipes):
			window.blit(game_images['pipeimage'][0],
						(upperPipe['x'], upperPipe['y']))
			window.blit(game_images['pipeimage'][1],
						(lowerPipe['x'], lowerPipe['y']))

		window.blit(game_images['sea_level'], (ground, elevation))
		window.blit(game_images['flappybird'], (horizontal, vertical))

		# Fetching the digits of score.
		numbers = [int(x) for x in list(str(your_score))]
		width = 0

		# finding the width of score images from numbers.
		for num in numbers:
			width += game_images['scoreimages'][num].get_width()
		Xoffset = (window_width - width)/1.1

		# Blitting the images on the window.
		for num in numbers:
			window.blit(game_images['scoreimages'][num],
						(Xoffset, window_width*0.02))
			Xoffset += game_images['scoreimages'][num].get_width()

		# Refreshing the game window and displaying the score.
		pygame.display.update()
		framepersecond_clock.tick(framepersecond)


def isGameOver(horizontal, vertical, up_pipes, down_pipes):
	if vertical > elevation - 25 or vertical < 0:
		return True

	for pipe in up_pipes:
		pipeHeight = game_images['pipeimage'][0].get_height()
		if(vertical < pipeHeight + pipe['y'] and\
		abs(horizontal - pipe['x']) < game_images['pipeimage'][0].get_width()):
			return True

	for pipe in down_pipes:
		if (vertical + game_images['flappybird'].get_height() > pipe['y']) and\
		abs(horizontal - pipe['x']) < game_images['pipeimage'][0].get_width():
			return True
	return False


def createPipe():
	offset = window_height/3
	pipeHeight = game_images['pipeimage'][0].get_height()
	y2 = offset + \
		random.randrange(
			0, int(window_height - game_images['sea_level'].get_height() - 1.2 * offset))
	pipeX = window_width + 10
	y1 = pipeHeight - y2 + offset
	pipe = [
		# upper Pipe
		{'x': pipeX, 'y': -y1},

		# lower Pipe
		{'x': pipeX, 'y': y2}
	]
	return pipe