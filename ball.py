from math import cos, sin


DEFAULT_BALL_COLOUR = (240, 240, 240)


class Ball:
	def __init__(self, pos=None, colour=DEFAULT_BALL_COLOUR):
		self.pos = pos
		self.colour = colour
		self.vel = (0, 0)

	def apply_force(self, mag, dir):
		x_vel = cos(dir) * mag
		y_vel = sin(dir) * mag
		self.vel = (self.vel[0] + x_vel, self.vel[1] + y_vel)

	def is_stationary(self):
		return self.vel == (0, 0)