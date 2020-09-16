from math import sqrt


DEFAULT_SURFACE_DRAG = 0.9
DEFAULT_HOLE_RADIUS = 5
BALL_VEL_EPSILON = 0.01


class Course:
	def __init__(self, ball, hole_pos):
		self.ball = ball
		self.hole_pos = hole_pos

	def update(self, time_delta):
		self.ball.pos = (self.ball.pos[0] + self.ball.vel[0] * time_delta, self.ball.pos[1] + self.ball.vel[1] * time_delta)
		self.ball.vel = (apply_epsilon(self.ball.vel[0] * DEFAULT_SURFACE_DRAG, BALL_VEL_EPSILON), apply_epsilon(self.ball.vel[1] * DEFAULT_SURFACE_DRAG, BALL_VEL_EPSILON))

	def is_complete(self):
		return calc_dist(self.ball.pos, self.hole_pos) <= DEFAULT_HOLE_RADIUS

def calc_dist(pt1, pt2):
	return sqrt((pt1[0] - pt2[0])**2 + (pt1[1] - pt2[1])**2)

def apply_epsilon(val, epsilon):
	return val if abs(val) > epsilon else 0