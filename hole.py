import collision_utils, commons


DEFAULT_SURFACE_DRAG = 0.9
DEFAULT_HOLE_RADIUS = 5
BALL_VEL_EPSILON = 0.01


class Hole:
	def __init__(self, ball_start_pos, hole_pos, golfer_start_direction, walls):
		self.ball_start_pos = ball_start_pos
		self.hole_pos = hole_pos
		self.golfer_start_direction = golfer_start_direction
		self.walls = walls

	def update(self, ball, time_delta=1):
		next_ball_pos = (ball.pos[0] + ball.vel[0] * time_delta, ball.pos[1] + ball.vel[1] * time_delta)
		next_ball_vel = (apply_epsilon(ball.vel[0] * DEFAULT_SURFACE_DRAG, BALL_VEL_EPSILON), apply_epsilon(ball.vel[1] * DEFAULT_SURFACE_DRAG, BALL_VEL_EPSILON))
	
		last_colliding_wall = None
		while True:
			colliding_wall = self._get_closest_colliding_wall(ball.pos, next_ball_pos, last_colliding_wall)
			if colliding_wall:
				next_ball_pos = colliding_wall.get_resultant_pos(ball.pos, next_ball_pos)
				next_ball_vel = colliding_wall.get_resultant_vel(next_ball_vel)
				ball.pos = colliding_wall.get_collision_pt(ball.pos, next_ball_pos) # use as temp storage
				last_colliding_wall = colliding_wall
			else:
				break
	
		ball.pos = next_ball_pos
		ball.vel = next_ball_vel
		
	def _get_closest_colliding_wall(self, pos1, pos2, last_colliding_wall):
		closest_colliding_wall = (None, 10000)
		for wall in self.walls:
			if wall.is_collision(pos1, pos2) and wall != last_colliding_wall:
				colliding_point = wall.get_collision_pt(pos1, pos2)
				dist = commons.get_dist(pos1, colliding_point)
				if dist < closest_colliding_wall[1]:
					closest_colliding_wall = (wall, dist)
		return closest_colliding_wall[0]

	def is_complete(self, ball):
		return commons.get_dist(ball.pos, self.hole_pos) <= DEFAULT_HOLE_RADIUS

def apply_epsilon(val, epsilon):
	return val if abs(val) > epsilon else 0