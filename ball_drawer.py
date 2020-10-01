import pygame


BALL_RADIUS = 2


class BallDrawer:
	def __init__(self):
		pass

	def draw(self, d_surf, ball):
		pygame.draw.circle(d_surf, ball.colour, (int(ball.pos[0]), int(ball.pos[1])), BALL_RADIUS)