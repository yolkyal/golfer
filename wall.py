class Wall:
	def __init__(self, pt1, pt2):
		self.pt1 = pt1
		self.pt2 = pt2
		self.is_horizontal = pt1[1] == pt2[1]
		self.is_vertical = pt1[0] == pt2[0]

	def is_collision(self, ball):
		if self.is_horizontal:
			return (ball.pos[1] < self.pt1[1]) is not ((ball.pos[1] + ball.vel[1]) < self.pt1[1]) and ball.pos[0] > self.pt1[0] and ball.pos[0] < self.pt2[0]
		elif self.is_vertical:
			return (ball.pos[0] < self.pt1[0]) is not ((ball.pos[0] + ball.vel[0]) < self.pt1[0]) and ball.pos[1] > self.pt1[1] and ball.pos[1] < self.pt2[1]
		else:
			return False

	def get_resultant_vel(self, ball):
		if self.is_horizontal:
			return (ball.vel[0], -ball.vel[1])
		elif self.is_vertical:
			return (-ball.vel[0], ball.vel[1])
		else:
			return ball.vel

	def get_resultant_pos(self, ball):
		if self.is_horizontal:
			dist_y = self.pos[1] - self.ball.pos[1]

		