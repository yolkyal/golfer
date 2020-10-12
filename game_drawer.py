class GameDrawer:
	def __init__(self, ball_drawer, golfer_drawer, hole_drawer, wall_drawer):
		self.ball_drawer = ball_drawer
		self.golfer_drawer = golfer_drawer
		self.hole_drawer = hole_drawer
		self.wall_drawer = wall_drawer

	def draw(self, d_surf, game):
		self.hole_drawer.draw(d_surf, game.hole)
		self.wall_drawer.draw(d_surf, game.hole.walls)
		self.golfer_drawer.draw(d_surf, game.golfer)
		self.ball_drawer.draw(d_surf, game.golfer.ball)