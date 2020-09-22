class Wall:
	def __init__(self, pt1, pt2):
		self.pt1 = pt1
		self.pt2 = pt2
		self.is_horizontal = pt1[1] == pt2[1]
		self.is_vertical = pt1[0] == pt2[0]

	def is_collision(self, pos1, pos2):
		if self.is_horizontal:
			return (pos1[1] < self.pt1[1]) is not (pos2[1] < self.pt1[1]) and pos1[0] >= self.pt1[0] and pos1[0] <= self.pt2[0]
		elif self.is_vertical:
			return (pos1[0] < self.pt1[0]) is not (pos2[0] < self.pt1[0]) and pos1[1] >= self.pt1[1] and pos1[1] <= self.pt2[1]
		else:
			return False

	def get_resultant_vel(self, vel):
		if self.is_horizontal:
			return (vel[0], -vel[1])
		elif self.is_vertical:
			return (-vel[0], vel[1])
		else:
			return ball.vel

	def get_resultant_pos(self, pos2):
		if self.is_horizontal:
			return (pos2[0], pos2[1] - 2 * (pos2[1] - self.pt1[1]))
		elif self.is_vertical:
			return (pos2[0] - 2 * (pos2[0] - self.pt1[0]), pos2[1])