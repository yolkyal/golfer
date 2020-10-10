import unittest
import game
from unittest import mock


class TestGame(unittest.TestCase):
	def setUp(self):
		self.golfer = mock.Mock()
		self.hole = mock.Mock()
		self.course = mock.Mock()
		self.course.holes = [self.hole]
		self.game = game.Game(self.golfer, self.course)

	def testUpdate(self):
		self.golfer.shot_count = 1
		self.hole.is_complete.return_value = True

		self.game.update()

		self.assertEqual([1], self.game.scores)
		self.assertTrue(self.game.is_complete())
		self.hole.update.assert_called_once()