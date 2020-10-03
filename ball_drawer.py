import pygame
import pygame.gfxdraw


BALL_RADIUS = 2


class BallDrawer:
	def __init__(self):
		pass

	def draw(self, d_surf, ball):
		pygame.gfxdraw.aacircle(d_surf, int(ball.pos[0]), int(ball.pos[1]), BALL_RADIUS, ball.colour)
		pygame.gfxdraw.filled_circle(d_surf, int(ball.pos[0]), int(ball.pos[1]), BALL_RADIUS, ball.colour)