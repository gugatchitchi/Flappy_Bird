import sys
import pygame
from pygame.locals import *
from Params import *
from Bird_Class import Bird
from Pipe_Class import Pipe

def game():

	# ==========================
	# Initialization of the game
	# ==========================

	# Set the score of the game to 0
	score = 0

	# Create bird from bird class
	bird = Bird()

	# Generate First batch of pipes
	pipes = [Pipe()]
	for i in range(9):
		pipes.append(Pipe(pipes[-1].X))

	# ===================================
	# Actual loop of the game starts here
	# ===================================
	while True:

		# if user clicks on cross button or escape key, the window will close
		for event in pygame.event.get():
			if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
				pygame.quit()
				sys.exit()

			# Player makes the bird go upwards (flap) by pressing space or upper_arrow
			if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
				bird.flap()

		# After each iteration/frame bird gravity pulls the bird down,
		# Pipes are moved left and we calculate the score
		bird.fall()
		pipes = pipes_iteration(pipes)
		score += update_score(pipes, bird)

		# print(len(pipes))


		# We redraw the window here
		draw(bird.X, bird.Y, pipes, score)

		# This code breaks the loop of player lost the game
		if check_colission(bird, pipes): break


# This function deals with collisions. It checks if bird left the window
# or has collided with any of the pipes
def check_colission(bird, pipes):
	# Check if bid crossed top and bottom boundaries
	if bird.Y < 0 or bird.Y > elevation:
		return True

	# Check if bird collided into one of the pipes
	for pipe in pipes:

		# Check left side of the bird, if it is inside pipes left and right X coordinates
		# and birds Y coordinates crossed pipes Y coordinates that means objects have collided
		if bird.X >= pipe.X and bird.X <= pipe.X + pipe_width:
			if bird.Y <= pipe.gap_Y or bird.Y + bird_height >= pipe.gap_Y + pipe_gap:
				return True

		# Check right side of the bird, if it is inside pipes left and right X coordinates
		# and birds Y coordinates crossed pipes Y coordinates that means objects have collided
		if bird.X + bird_width >= pipe.X and bird.X + bird_width <= pipe.X + pipe_width:
			if bird.Y <= pipe.gap_Y or bird.Y + bird_height >= pipe.gap_Y + pipe_gap:
				return True



# This function deals with pipes. It moves all the pipes,
# pops the pipes from the list, which left the window
# and adds new pipes to the list
def pipes_iteration(pipes):

	# Move each pipe
	for pipe in pipes:
		pipe.move()

	# Filter pipes which left the window
	pipes = list(filter(lambda pipe: pipe.X + game_images['pipeimage'][0].get_width() > 0, pipes))

	# Add new pipes to the list if the count is less than 10
	if len(pipes) < 10:
		pipes.append(Pipe(pipes[-1].X))

	# Finally, we return the new pipes list
	return pipes



# If the bird has recently passed the gap between the pipes
# this function returns 1, else it returns 0
def update_score(pipes, bird):

	for pipe in pipes:
		# Check left side of the bird, if it was inside pipes left and right X coordinates
		# one iteration ago, and now it has passed it, that means bird gets a score
		if pipe.X + pipe_width <= bird.X <= pipe.X + pipe_width + pipe_velocity:
				return 1

	# If it not the case score stays the same
	return 0



# This function paints the background and bird on the screen
# Until the player enters necessary key to start the game
# Bird will be frozen in one place.
def draw(bird_x = bird_initial_X, bird_y = bird_initial_Y, pipes = None, score = None):

	# Add images on the window
	window.blit(game_images['background'], (0, 0))
	window.blit(game_images['sea_level'], (ground, elevation))
	window.blit(game_images['flappybird'], (bird_x, bird_y))

	if pipes is not None:
		for pipe in pipes:
			window.blit(game_images['pipeimage'][0], (pipe.X, pipe.get_Y_coordinates()[0]))
			window.blit(game_images['pipeimage'][1], (pipe.X, pipe.get_Y_coordinates()[1]))

	# Display Score
	font = pygame.font.SysFont('Comic Sans MS', 30)
	text = font.render('Score: ' + str(score), False, (0, 0, 0))
	window.blit(text, (0,0))

	# Update the window
	pygame.display.update()
	framepersecond_clock.tick(framepersecond)