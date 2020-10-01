import pygame


DEFAULT_HOLE_COLOUR = (50, 50, 50)
DEFAULT_HOLE_RADIUS = 5


class HoleDrawer:
	def __init__(self):
		pass

	def draw(self, d_surf, hole):
		pygame.draw.circle(d_surf, DEFAULT_HOLE_COLOUR, hole.hole_pos, DEFAULT_HOLE_RADIUS)