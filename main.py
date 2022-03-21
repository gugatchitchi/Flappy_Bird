import pygame
from pygame.locals import *
from Logic import *

# program where the game starts
if __name__ == "__main__":

	# For initializing modules of pygame library
	pygame.init()
	pygame.font.init()

	# Sets the title on top of game window
	pygame.display.set_caption(title)

	# Printing the welcome text
	print("WELCOME TO THE FLAPPY BIRD GAME")
	print("Press space or enter to start the game")

	# Initilize max score as 0
	max_score = 0

	# Waiting for user to start the game
	while True:

		# Catching events from user
		for event in pygame.event.get():

			# if user clicks on cross button or escape key, the window will close
			if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
				pygame.quit()
				sys.exit()

			# Player can start playing by pressing space or up arrow key
			elif event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
				max_score = game(max_score)
				print(max_score)

			# if user doesn't press any key we show the frozen frame
			else:
				draw(max_score = max_score)

