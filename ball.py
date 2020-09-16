from math import cos, sin


class Ball:
	def __init__(self, pos):
		self.pos = pos
		self.vel = (0, 0)

	def apply_force(self, mag, dir):
		x_vel = cos(dir) * mag
		y_vel = sin(dir) * mag
		self.vel = (self.vel[0] + x_vel, self.vel[1] + y_vel)

	def is_stationary(self):
		return self.vel == (0, 0)