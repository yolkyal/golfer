import unittest
import hole_drawer
from unittest import mock


class TestHoleDrawer(unittest.TestCase):
	def setUp(self):
		self.d_surf = mock.Mock()
		self.hole = mock.Mock()
		self.hole_drawer = hole_drawer.HoleDrawer()

	@mock.patch('pygame.gfxdraw.filled_circle')
	@mock.patch('pygame.gfxdraw.aacircle')
	def testDraw(self, mock_draw_aacircle, mock_draw_filled_circle):
		self.hole.hole_pos = (0, 0)
	
		self.hole_drawer.draw(self.d_surf, self.hole)

		mock_draw_aacircle.assert_called_once_with(self.d_surf, self.hole.hole_pos[0], self.hole.hole_pos[1], hole_drawer.DEFAULT_HOLE_RADIUS, hole_drawer.DEFAULT_HOLE_COLOUR)
		mock_draw_filled_circle.assert_called_once_with(self.d_surf, self.hole.hole_pos[0], self.hole.hole_pos[1], hole_drawer.DEFAULT_HOLE_RADIUS, hole_drawer.DEFAULT_HOLE_COLOUR)