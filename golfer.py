import math, datetime


TURN_ANGLE = math.pi / 128
SWING_FORCE_TIME_MULTIPLIER = 0.5
SWING_TIME_LIMIT = datetime.timedelta(seconds=2)
MAX_MAG = SWING_FORCE_TIME_MULTIPLIER * SWING_TIME_LIMIT.seconds


class Golfer:
	def __init__(self, ball, direction=0):
		self.ball = ball
		self.direction = direction
		self.turning_left = False
		self.turning_right = False
		self.start_swing_time = None
		self.end_swing_time = None

	def start_turn_left(self):
		self.turning_left = True

	def end_turn_left(self):
		self.turning_left = False

	def start_turn_right(self):
		self.turning_right = True

	def end_turn_right(self):
		self.turning_right = False

	def start_swing(self):
		if self.ball.is_stationary():
			self.start_swing_time = datetime.datetime.now()

	def end_swing(self):
		if self.start_swing_time:
			self.end_swing_time = datetime.datetime.now()

	def get_active_swing_time(self):
		if self.start_swing_time and not self.end_swing_time:
			time_delta = datetime.datetime.now() - self.start_swing_time
			return time_delta.seconds + time_delta.microseconds / 1000000

	def get_completed_swing_time(self):
		if self.start_swing_time and self.end_swing_time:
			time_delta = self.end_swing_time - self.start_swing_time
			return time_delta.seconds + time_delta.microseconds / 1000000

	def update(self):
		if not self.ball.is_stationary():
			return # no updates allowed while ball is moving

		if not self.start_swing_time:
			if self.turning_left:
				self.direction -= TURN_ANGLE
			if self.turning_right:
				self.direction += TURN_ANGLE

		if self.start_swing_time:
			if self.end_swing_time:
				time_delta = self.end_swing_time - self.start_swing_time
				mag = self.get_completed_swing_time() * SWING_FORCE_TIME_MULTIPLIER
				self.ball.apply_force(mag, self.direction)
				self.start_swing_time = None
				self.end_swing_time = None
			elif datetime.datetime.now() - self.start_swing_time >= SWING_TIME_LIMIT:
				self.ball.apply_force(MAX_MAG, self.direction)
				self.start_swing_time = None