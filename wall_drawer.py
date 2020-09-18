import pygame


DEFAULT_WALL_COLOUR = (150, 150, 150)

		
class WallDrawer:
	def __init__(self):
		pass
		
	def draw(self, d_surf, wall):
		pygame.draw.line(d_surf, DEFAULT_WALL_COLOUR, wall.pt1, wall.pt2)