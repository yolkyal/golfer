import unittest
import wall
from unittest import mock


class TestWall(unittest.TestCase):
	def setUp(self):
		self.ball = mock.Mock()

	def testCollisionVerticalWall(self):
		self.wall = wall.Wall((100, 0), (100, 100))

		self.ball.pos = (99, 50)
		self.ball.vel = (1.5, 0)
		self.assertTrue(self.wall.is_collision(self.ball))

		self.ball.pos = (99, 101)
		self.ball.vel = (1.5, 0)
		self.assertFalse(self.wall.is_collision(self.ball))

		self.ball.pos = (101, 50)
		self.ball.vel = (-1.5, 0)
		self.assertTrue(self.wall.is_collision(self.ball))

		self.ball.pos = (99, -1)
		self.ball.vel = (1.5, 0)
		self.assertFalse(self.wall.is_collision(self.ball))

	def testResultantPosVerticalWall(self):
		self.wall = wall.Wall((100, 0), (100, 100))

		self.ball.pos = (99, 50)
		self.ball.vel = (1.5, 0)
		self.assertEqual((99.5, 50), self.wall.get_resultant_pos(self.ball))

		self.ball.pos = (101, 50)
		self.ball.vel = (-1.5, 0)
		self.assertEqual((100.5, 50), self.wall.get_resultant_pos(self.ball))

	def testResultantVelVerticalWall(self):
		self.wall = wall.Wall((100, 0), (100, 100))

		self.ball.pos = (99, 50)
		self.ball.vel = (1.5, 0)
		self.assertEqual((-1.5, 0), self.wall.get_resultant_vel(self.ball))

		self.ball.pos = (101, 50)
		self.ball.vel = (-1.5, 0)
		self.assertEqual((1.5, 0), self.wall.get_resultant_vel(self.ball))

	def testCollisionHorizontalWall(self):
		self.wall = wall.Wall((0, 100), (100, 100))

		self.ball.pos = (50, 99)
		self.ball.vel = (0, 1.5)
		self.assertTrue(self.wall.is_collision(self.ball))

		self.ball.pos = (101, 99)
		self.ball.vel = (0, 1.5)
		self.assertFalse(self.wall.is_collision(self.ball))

		self.ball.pos = (50, 101)
		self.ball.vel = (0, -1.5)
		self.assertTrue(self.wall.is_collision(self.ball))

		self.ball.pos = (-1, 99)
		self.ball.vel = (0, 1.5)
		self.assertFalse(self.wall.is_collision(self.ball))

	def testResultantPosHorizontalWall(self):
		self.wall = wall.Wall((0, 100), (100, 100))

		self.ball.pos = (50, 99)
		self.ball.vel = (0, 1.5)
		self.assertEqual((50, 99.5), self.wall.get_resultant_pos(self.ball))

		self.ball.pos = (50, 101)
		self.ball.vel = (0, -1.5)
		self.assertEqual((50, 100.5), self.wall.get_resultant_pos(self.ball))

	def testResultantVelHorizontalWall(self):
		self.wall = wall.Wall((0, 100), (100, 100))

		self.ball.pos = (50, 99)
		self.ball.vel = (0, 1.5)
		self.assertEqual((0, -1.5), self.wall.get_resultant_vel(self.ball))

		self.ball.pos = (50, 101)
		self.ball.vel = (0, -1.5)
		self.assertEqual((0, 1.5), self.wall.get_resultant_vel(self.ball))