import unittest
import hole_drawer
from unittest import mock


class TestHoleDrawer(unittest.TestCase):
	def setUp(self):
		self.d_surf = mock.Mock()
		self.hole = mock.Mock()
		self.hole_drawer = hole_drawer.HoleDrawer()

	@mock.patch('pygame.draw.circle')
	def testDraw(self, mock_draw_circle):
		self.hole_drawer.draw(self.d_surf, self.hole)

		mock_draw_circle.assert_called_once_with(self.d_surf, hole_drawer.DEFAULT_HOLE_COLOUR, self.hole.hole_pos, hole_drawer.DEFAULT_HOLE_RADIUS)