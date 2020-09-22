import unittest
import course
from unittest import mock


class TestCourse(unittest.TestCase):
	def setUp(self):
		self.hole_pos = (0, 0)
		self.ball = mock.Mock()
		self.wall = mock.Mock()
		self.wall.is_collision.return_value = False
		self.course = course.Course(self.ball, self.hole_pos, [self.wall])

	def testUpdate(self):
		self.ball.pos = (1, 2)
		self.ball.vel = (3, 4)
		time_delta = 2

		expected_ball_pos = (self.ball.pos[0] + self.ball.vel[0] * time_delta, self.ball.pos[1] + self.ball.vel[1] * time_delta)
		expected_ball_vel = (self.ball.vel[0] * course.DEFAULT_SURFACE_DRAG, self.ball.vel[1] * course.DEFAULT_SURFACE_DRAG)

		self.course.update(time_delta)

		self.assertEqual(expected_ball_pos, self.ball.pos)
		self.assertEqual(expected_ball_vel, self.ball.vel)
		
	def testUpdateWithWallCollision(self):
		self.wall.is_collision.return_value = True
		
		self.course.update(1)
		
		self.wall.get_resultant_vel.assert_called_once_with(self.ball)
		self.wall.get_resultant_pos.assert_called_once_with(self.ball)
		self.assertEqual(self.ball.vel, self.wall.get_resultant_vel(self.ball))
		self.assertEqual(self.ball.pos, self.wall.get_resultant_pos(self.ball))

	def testIsComplete(self):
		self.ball.pos = (0, course.DEFAULT_HOLE_RADIUS)

		self.assertTrue(self.course.is_complete())