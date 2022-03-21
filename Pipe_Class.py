from Params import *
import random

class Pipe:
  def __init__(self, previous_pipe_X = window_width):
    self.X = previous_pipe_X + random.randrange(min_distance_between_pipes, max_distance_between_pipes)
    self.gap_Y = random.randrange(pipe_gap_y_min, pipe_gap_y_max)

  # After each iteration all pipes move left on the screen
  def move(self):
    self.X -= pipe_velocity

  # We need these weird Y coordinated to put images in the right place
  # This function gives information where the upper and lower pipes picture
  # should be put on the Y axis
  def get_Y_coordinates(self):
    upper_Y = self.gap_Y - game_images['pipeimage'][0].get_height()
    lower_Y = self.gap_Y + pipe_gap
    return upper_Y, lower_Y