import unittest
import wall_drawer
from unittest import mock


class TestWallDrawer(unittest.TestCase):
	def setUp(self):
		self.d_surf = mock.Mock()
		self.wall1 = mock.Mock(pt1=(0, 0), pt2=(1, 1))
		self.wall2 = mock.Mock(pt1=(2, 2), pt2=(3, 3))
		self.wall_drawer = wall_drawer.WallDrawer()
	
	@mock.patch('pygame.draw.line')
	def testDraw(self, mock_draw_line):
		
		self.wall_drawer.draw(self.d_surf, [self.wall1])
		
		mock_draw_line.assert_called_once_with(self.d_surf, wall_drawer.DEFAULT_WALL_COLOUR, self.wall1.pt1, self.wall1.pt2)

	@mock.patch('pygame.draw.line')
	def testDrawMultiple(self, mock_draw_line):
		self.wall_drawer.draw(self.d_surf, [self.wall1, self.wall2])

		expected_line_calls = [
		mock.call(self.d_surf, wall_drawer.DEFAULT_WALL_COLOUR, self.wall1.pt1, self.wall1.pt2),
		mock.call(self.d_surf, wall_drawer.DEFAULT_WALL_COLOUR, self.wall2.pt1, self.wall2.pt2)
		]
		
		self.assertEqual(expected_line_calls, mock_draw_line.call_args_list)