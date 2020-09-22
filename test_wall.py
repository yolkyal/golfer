import unittest
import wall
from unittest import mock


class TestWall(unittest.TestCase):
	def setUp(self):
		self.vertical_wall = wall.Wall((100, 0), (100, 100))
		self.horizontal_wall = wall.Wall((0, 100), (100, 100))
		self.ball = mock.Mock()

	def testCollisionVerticalWall(self):
		pos1 = (99, 100)
		pos2 = (100.5, 100)
		self.assertTrue(self.vertical_wall.is_collision(pos1, pos2))

		pos1 = (99, 101)
		pos2 = (100.5, 101)
		self.assertFalse(self.vertical_wall.is_collision(pos1, pos2))

		pos1 = (101, 0)
		pos2 = (99.5, 0)
		self.assertTrue(self.vertical_wall.is_collision(pos1, pos2))

		pos1 = (101, -1)
		pos2 = (99.5, -1)
		self.assertFalse(self.vertical_wall.is_collision(pos1, pos2))

	def testResultantPosVerticalWall(self):
		pos2 = (100.5, 50)
		self.assertEqual((99.5, 50), self.vertical_wall.get_resultant_pos(pos2))

		pos2 = (99.5, 50)
		self.assertEqual((100.5, 50), self.vertical_wall.get_resultant_pos(pos2))

	def testResultantVelVerticalWall(self):
		vel = (1.5, 0)
		self.assertEqual((-1.5, 0), self.vertical_wall.get_resultant_vel(vel))

		vel = (-1.5, 0)
		self.assertEqual((1.5, 0), self.vertical_wall.get_resultant_vel(vel))

	def testCollisionHorizontalWall(self):
		pos1 = (50, 99)
		pos2 = (50, 100.5)
		self.assertTrue(self.horizontal_wall.is_collision(pos1, pos2))

		pos1 = (101, 99)
		pos2 = (101, 100.5)
		self.assertFalse(self.horizontal_wall.is_collision(pos1, pos2))

		pos1 = (50, 101)
		pos2 = (50, 99.5)
		self.assertTrue(self.horizontal_wall.is_collision(pos1, pos2))

		pos1 = (-1, 99)
		pos2 = (-1, 100.5)
		self.assertFalse(self.horizontal_wall.is_collision(pos1, pos2))

	def testResultantPosHorizontalWall(self):
		pos2 = (50, 100.5)
		self.assertEqual((50, 99.5), self.horizontal_wall.get_resultant_pos(pos2))

		pos2 = (50, 99.5)
		self.assertEqual((50, 100.5), self.horizontal_wall.get_resultant_pos(pos2))

	def testResultantVelHorizontalWall(self):
		vel = (0, 1.5)
		self.assertEqual((0, -1.5), self.horizontal_wall.get_resultant_vel(vel))

		vel = (0, -1.5)
		self.assertEqual((0, 1.5), self.horizontal_wall.get_resultant_vel(vel))