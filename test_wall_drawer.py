import unittest
import wall_drawer
from unittest import mock


class TestWallDrawer(unittest.TestCase):
	def setUp(self):
		self.d_surf = mock.Mock()
		self.wall = mock.Mock()
		self.wall_drawer = wall_drawer.WallDrawer()
	
	@mock.patch('pygame.draw.line')
	def testDraw(self, mock_draw_line):
		self.wall.pt1 = (0, 0)
		self.wall.pt2 = (100, 100)
		
		self.wall_drawer.draw(self.d_surf, self.wall)
		
		mock_draw_line.assert_called_once_with(self.d_surf, wall_drawer.DEFAULT_WALL_COLOUR, self.wall.pt1, self.wall.pt2)