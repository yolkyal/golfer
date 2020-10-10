class Game:
	def __init__(self, golfer, course):
		self.golfer = golfer
		self.course = course
		self.hole_number = 0
		self._start_new_hole()
		self.scores = [0] * len(self.course.holes)

	def update(self, delta_ms):
		self.golfer.update()
		self.hole.update(self.golfer.ball, delta_ms)

		if self.hole.is_complete(self.golfer.ball):
			self.scores[self.hole_number] = self.golfer.shot_count
			self.hole_number += 1
			if self.hole_number < len(self.course.holes):
				self._start_new_hole()

	def is_complete(self):
		return self.hole_number >= len(self.course.holes)

	def _start_new_hole(self):
		self.hole = self.course.holes[self.hole_number]
		self.golfer.reset_shot_count()
		self.golfer.ball.pos = self.hole.ball_start_pos
		self.golfer.direction = self.hole.golfer_start_direction