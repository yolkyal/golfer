import unittest
import game_drawer
from unittest import mock


class TestGameDrawer(unittest.TestCase):
	def setUp(self):
		self.game = mock.Mock()
		self.ball_drawer = mock.Mock()
		self.golfer_drawer = mock.Mock()
		self.hole_drawer = mock.Mock()
		self.wall_drawer = mock.Mock()
		self.game_drawer = game_drawer.GameDrawer(self.ball_drawer, self.golfer_drawer, self.hole_drawer, self.wall_drawer)

	def testDraw(self):
		d_surf = mock.Mock()
		self.game_drawer.draw(d_surf, self.game)

		self.ball_drawer.draw.assert_called_with(d_surf, self.game.golfer.ball)
		self.golfer_drawer.draw.assert_called_with(d_surf, self.game.golfer)
		self.hole_drawer.draw.assert_called_with(d_surf, self.game.hole)
		self.wall_drawer.draw.assert_called_with(d_surf, self.game.hole.walls)