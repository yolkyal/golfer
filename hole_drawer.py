import pygame
import pygame.gfxdraw


DEFAULT_HOLE_COLOUR = (50, 50, 50)
DEFAULT_HOLE_RADIUS = 5


class HoleDrawer:
	def __init__(self):
		pass

	def draw(self, d_surf, hole):
		pygame.gfxdraw.aacircle(d_surf, hole.hole_pos[0], hole.hole_pos[1], DEFAULT_HOLE_RADIUS, DEFAULT_HOLE_COLOUR)
		pygame.gfxdraw.filled_circle(d_surf, hole.hole_pos[0], hole.hole_pos[1], DEFAULT_HOLE_RADIUS, DEFAULT_HOLE_COLOUR)