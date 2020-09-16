import unittest
import ball_drawer
from unittest import mock


class TestBallDrawer(unittest.TestCase):
	def setUp(self):
		self.d_surf = mock.Mock()
		self.ball_drawer = ball_drawer.BallDrawer()

	@mock.patch('pygame.draw.circle')
	def testDraw(self, mock_draw_circle):
		ball = mock.Mock()
		ball.pos = (0, 0)

		self.ball_drawer.draw(self.d_surf, ball)

		mock_draw_circle.assert_called_once_with(self.d_surf, ball_drawer.DEFAULT_BALL_COLOUR, ball.pos, ball_drawer.BALL_RADIUS)