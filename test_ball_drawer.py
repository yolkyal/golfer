import unittest
import ball_drawer
from unittest import mock


class TestBallDrawer(unittest.TestCase):
	def setUp(self):
		self.d_surf = mock.Mock()
		self.ball_drawer = ball_drawer.BallDrawer()

	@mock.patch('pygame.gfxdraw.filled_circle')
	@mock.patch('pygame.gfxdraw.aacircle')
	def testDraw(self, mock_draw_aacircle, mock_draw_filled_circle):
		ball = mock.Mock()
		ball.pos = (0, 0)

		self.ball_drawer.draw(self.d_surf, ball)

		mock_draw_aacircle.assert_called_once_with(self.d_surf, ball.pos[0], ball.pos[1], ball_drawer.BALL_RADIUS, ball.colour)
		mock_draw_filled_circle.assert_called_once_with(self.d_surf, ball.pos[0], ball.pos[1], ball_drawer.BALL_RADIUS, ball.colour)