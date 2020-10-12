import pygame


DEFAULT_WALL_COLOUR = (220, 220, 220)

		
class WallDrawer:
	def __init__(self):
		pass

	def draw(self, d_surf, walls):
		for wall in walls:
			pygame.draw.line(d_surf, DEFAULT_WALL_COLOUR, wall.pt1, wall.pt2)