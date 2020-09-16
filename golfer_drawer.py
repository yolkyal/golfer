import pygame
import math


DEFAULT_GUIDE_LINE_COLOUR = (50, 50, 50)
DEFAULT_POWER_LINE_COLOUR = (220, 220, 220)
SWING_TIME_ARC_SCALER = 50
SWING_ARC_ANGLE = math.pi / 64
GUIDE_LINE_LENGTH = 100


class GolferDrawer:
	def __init__(self):
		pass

	def draw(self, d_surf, golfer):
		if golfer.ball.is_stationary():
			guide_line_endx = golfer.ball.pos[0] + GUIDE_LINE_LENGTH * math.cos(golfer.direction)
			guide_line_endy = golfer.ball.pos[1] + GUIDE_LINE_LENGTH * math.sin(golfer.direction)
			pygame.draw.aaline(d_surf, DEFAULT_GUIDE_LINE_COLOUR, golfer.ball.pos, (guide_line_endx, guide_line_endy))

			active_swing_time = golfer.get_active_swing_time()
			if active_swing_time:
				power_line_length = active_swing_time / 2 * GUIDE_LINE_LENGTH
				power_line_endx = golfer.ball.pos[0] + power_line_length * math.cos(golfer.direction)
				power_line_endy = golfer.ball.pos[1] + power_line_length * math.sin(golfer.direction)
				pygame.draw.aaline(d_surf, DEFAULT_POWER_LINE_COLOUR, golfer.ball.pos, (power_line_endx, power_line_endy))