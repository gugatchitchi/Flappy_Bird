import pygame
from pygame.locals import *
from Logic import *

# program where the game starts
if __name__ == "__main__":

	# For initializing modules of pygame library
	pygame.init()

	# Sets the title on top of game window
	pygame.display.set_caption(title)

	# Printing the welcome text
	print("WELCOME TO THE FLAPPY BIRD GAME")
	print("Press space or enter to start the game")

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
				flappygame()

			# if user doesn't press any key we show the frozen frame
			else:
				Draw()

