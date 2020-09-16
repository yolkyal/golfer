import unittest, pygame
import golfer_controller
from unittest import mock


class TestGolferController(unittest.TestCase):
	def setUp(self):
		self.golfer = mock.Mock()
		self.golfer_controller = golfer_controller.GolferController(self.golfer)

	def testKeyDownKLeft(self):
		e = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_LEFT)

		self.golfer_controller.handle_event(e)

		self.golfer.start_turn_left.assert_called_once()

	def testKeyUpKLeft(self):
		e = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_LEFT)

		self.golfer_controller.handle_event(e)

		self.golfer.start_turn_left.assert_called_once()

	def testKeyDownKRight(self):
		e = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_RIGHT)
		
		self.golfer_controller.handle_event(e)

		self.golfer.start_turn_right.assert_called_once()

	def testKeyUpKRight(self):
		e = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_RIGHT)
		
		self.golfer_controller.handle_event(e)

		self.golfer.start_turn_right.assert_called_once()

	def testKeyDownKUp(self):
		e = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_UP)
		
		self.golfer_controller.handle_event( e)

		self.golfer.start_swing.assert_called_once()

	def testKeyUpKUp(self):
		e = pygame.event.Event(pygame.KEYUP, key=pygame.K_UP)
		
		self.golfer_controller.handle_event(e)

		self.golfer.end_swing.assert_called_once()