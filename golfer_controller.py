import pygame


class GolferController:
	def __init__(self, golfer):
		self.golfer = golfer

	def handle_event(self, e):
		if e.type == pygame.KEYDOWN:
			if e.key == pygame.K_LEFT:
				self.golfer.start_turn_left()
			elif e.key == pygame.K_RIGHT:
				self.golfer.start_turn_right()
			elif e.key == pygame.K_UP:
				self.golfer.start_swing()
		elif e.type == pygame.KEYUP:
			if e.key == pygame.K_LEFT:
				self.golfer.end_turn_left()
			elif e.key == pygame.K_RIGHT:
				self.golfer.end_turn_right()
			if e.key == pygame.K_UP:
				self.golfer.end_swing()