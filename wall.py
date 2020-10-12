import collision_utils
import math

class Wall:
	def __init__(self, pt1, pt2):
		self.pt1 = pt1
		self.pt2 = pt2
		self.is_horizontal = pt1[1] == pt2[1]
		self.is_vertical = pt1[0] == pt2[0]
		self.angle = math.atan((pt2[1] - pt1[1]) / (pt2[0] - pt1[0])) if not self.is_vertical else math.pi / 2

	def __eq__(self, other):
		return other is not None and self.pt1 == other.pt1 and self.pt2 == other.pt2

	def is_collision(self, pos1, pos2):
		return collision_utils.is_line_intersection(self.pt1, self.pt2, pos1, pos2)
		
	def get_collision_pt(self, pos1, pos2):
		return collision_utils.get_line_intersection_pt(self.pt1, self.pt2, pos1, pos2)
			
	def get_resultant_pos(self, pos1, pos2):
		line_intersection_pt = self.get_collision_pt(pos1, pos2)
		tmp_pt = (pos2[0] - line_intersection_pt[0], pos2[1] - line_intersection_pt[1])
		ref_pt = (math.cos(2 * self.angle) * tmp_pt[0] + math.sin(2 * self.angle) * tmp_pt[1], math.sin(2 * self.angle) * tmp_pt[0] - math.cos(2 * self.angle) * tmp_pt[1])
		return (ref_pt[0] + line_intersection_pt[0], ref_pt[1] + line_intersection_pt[1])
		
	def get_resultant_vel(self, vel):
		return (math.cos(2 * self.angle) * vel[0] + math.sin(2 * self.angle) * vel[1], math.sin(2 * self.angle) * vel[0] - math.cos(2 * self.angle) * vel[1])

			
class WallBuilder:
	def __init__(self, *pts):
		self.pts = pts
	
	def build(self):
		results = []
		for i in range(len(self.pts) - 1):
			results.append(Wall(self.pts[i], self.pts[i + 1]))
		results.append(Wall(self.pts[len(self.pts) - 1], self.pts[0]))

		return results