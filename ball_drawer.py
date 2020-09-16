import pygame


BALL_RADIUS = 2
DEFAULT_BALL_COLOUR = (240, 240, 240)


class BallDrawer:
	def __init__(self):
		pass

	def draw(self, d_surf, ball):
		pygame.draw.circle(d_surf, DEFAULT_BALL_COLOUR, (int(ball.pos[0]), int(ball.pos[1])), BALL_RADIUS)