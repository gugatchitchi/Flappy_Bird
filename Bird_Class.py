from Params import *

class Bird:
  def __init__(self):
    self.X = bird_initial_X
    self.Y = bird_initial_Y
    self.velocity = bird_min_velocity

  # When users input is detected we try to decrease birds velocity
  # to give an impression that it jumps. While doing so we should
  # check that the velocity is not less than min_velocity value,
  # not to "overjump" the screen after multiple inputs
  def flap(self):
    self.velocity = bird_min_velocity

  # For each frame we try to increase birds velocity
  # to give an impression that it drops. While doing so we should
  # check that the velocity is not more than max_velocity value,
  # not to cause uncontrolled acceleration to the ground
  def fall(self):
    if self.velocity + gravity_velocity_change > bird_max_velocity:
      self.velocity = bird_max_velocity
    else:
      self.velocity += gravity_velocity_change

    # We Update coordinates here as this function will be called
    # after each frame/iteration
    self.Y += self.velocity

