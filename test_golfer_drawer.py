import unittest, math
import golfer_drawer
from unittest import mock


class TestGolferDrawer(unittest.TestCase):
	def setUp(self):
		self.d_surf = mock.Mock()
		self.golfer = mock.Mock()
		self.golfer.ball.pos = (0, 0)
		self.golfer.ball.is_stationary.return_value = True
		self.golfer.direction = 1
		self.golfer_drawer = golfer_drawer.GolferDrawer()

	@mock.patch('pygame.draw.aaline')
	def testDrawInactive(self, mock_draw_line):
		self.golfer.get_active_swing_time.return_value = None

		self.golfer_drawer.draw(self.d_surf, self.golfer)

		guide_line_end_pos = (math.cos(self.golfer.direction) * golfer_drawer.GUIDE_LINE_LENGTH, math.sin(self.golfer.direction) * golfer_drawer.GUIDE_LINE_LENGTH)
		mock_draw_line.assert_called_once_with(self.d_surf, golfer_drawer.DEFAULT_GUIDE_LINE_COLOUR, self.golfer.ball.pos, guide_line_end_pos)

	@mock.patch('pygame.draw.aaline')
	def testDrawActiveSwing(self, mock_draw_line):
		self.golfer.get_active_swing_time.return_value = 1.5

		self.golfer_drawer.draw(self.d_surf, self.golfer)

		power_line_length = golfer_drawer.GUIDE_LINE_LENGTH * 0.75
		power_line_end_pos = (math.cos(self.golfer.direction) * power_line_length, math.sin(self.golfer.direction) * power_line_length)
		guide_line_end_pos = (math.cos(self.golfer.direction) * golfer_drawer.GUIDE_LINE_LENGTH, math.sin(self.golfer.direction) * golfer_drawer.GUIDE_LINE_LENGTH)

		expected_line_calls = [
		mock.call(self.d_surf, golfer_drawer.DEFAULT_GUIDE_LINE_COLOUR, self.golfer.ball.pos, guide_line_end_pos),
		mock.call(self.d_surf, golfer_drawer.DEFAULT_POWER_LINE_COLOUR, self.golfer.ball.pos, power_line_end_pos)
		]

		self.assertEqual(expected_line_calls, mock_draw_line.call_args_list)

	@mock.patch('pygame.draw.aaline')
	def testDrawWithMovingBall(self, mock_draw_line):
		self.golfer.ball.is_stationary.return_value = False

		self.golfer_drawer.draw(self.d_surf, self.golfer)

		mock_draw_line.assert_not_called()