import unittest
import wall
from unittest import mock


class TestWall(unittest.TestCase):
	def setUp(self):
		self.vertical_wall = wall.Wall((100, 0), (100, 100))
		self.horizontal_wall = wall.Wall((0, 100), (100, 100))
		self.deg45_wall = wall.Wall((50, 50), (100, 100))
		self.ball = mock.Mock()

	def testCollisionVerticalWall(self):
		pos1 = (99, 99)
		pos2 = (100.5, 99)
		self.assertTrue(self.vertical_wall.is_collision(pos1, pos2))

		pos1 = (99, 101)
		pos2 = (100.5, 101)
		self.assertFalse(self.vertical_wall.is_collision(pos1, pos2))

		pos1 = (101, 1)
		pos2 = (99.5, 1)
		self.assertTrue(self.vertical_wall.is_collision(pos1, pos2))

		pos1 = (101, -1)
		pos2 = (99.5, -1)
		self.assertFalse(self.vertical_wall.is_collision(pos1, pos2))
		
		pos1 = (99, 0)
		pos2 = (101, 5)
		self.assertTrue(self.vertical_wall.is_collision(pos1, pos2))

	def testResultantPosVerticalWall(self):
		pos1 = (99.5, 50)
		pos2 = (100.5, 50)
		self.assertEqual((99.5, 50), self.vertical_wall.get_resultant_pos(pos1, pos2))

		pos1 = (100.5, 50)
		pos2 = (99.5, 50)
		self.assertEqual((100.5, 50), self.vertical_wall.get_resultant_pos(pos1, pos2))

	def testResultantVelVerticalWall(self):
		vel = (1.5, 0)
		self.assertAlmostEqualTup((-1.5, 0), self.vertical_wall.get_resultant_vel(vel))

		vel = (-1.5, 0)
		self.assertAlmostEqualTup((1.5, 0), self.vertical_wall.get_resultant_vel(vel))

	def testCollisionHorizontalWall(self):
		pos1 = (99, 99)
		pos2 = (99, 100.5)
		self.assertTrue(self.horizontal_wall.is_collision(pos1, pos2))

		pos1 = (101, 99)
		pos2 = (101, 100.5)
		self.assertFalse(self.horizontal_wall.is_collision(pos1, pos2))

		pos1 = (1, 101)
		pos2 = (1, 99.5)
		self.assertTrue(self.horizontal_wall.is_collision(pos1, pos2))

		pos1 = (-1, 99)
		pos2 = (-1, 100.5)
		self.assertFalse(self.horizontal_wall.is_collision(pos1, pos2))
		
		pos1 = (101, 99)
		pos2 = (95, 101)
		self.assertTrue(self.vertical_wall.is_collision(pos1, pos2))

	def testResultantPosHorizontalWall(self):
		pos1 = (50, 99.5)
		pos2 = (50, 100.5)
		self.assertEqual((50, 99.5), self.horizontal_wall.get_resultant_pos(pos1, pos2))

		pos1 = (50, 100.5)
		pos2 = (50, 99.5)
		self.assertEqual((50, 100.5), self.horizontal_wall.get_resultant_pos(pos1, pos2))

	def testResultantVelHorizontalWall(self):
		vel = (0, 1.5)
		self.assertAlmostEqualTup((0, -1.5), self.horizontal_wall.get_resultant_vel(vel))

		vel = (0, -1.5)
		self.assertAlmostEqualTup((0, 1.5), self.horizontal_wall.get_resultant_vel(vel))
		
	def testResultantPosWall(self):
		pos1 = (75, 100)
		pos2 = (75, 50)
		self.assertEqual((50, 75), self.deg45_wall.get_resultant_pos(pos1, pos2))
		
		pos2 = (100, 75)
		self.assertEqual((75, 100), self.deg45_wall.get_resultant_pos(pos1, pos2))
		
	def testResultantVelDeg45Wall(self):
		vel = (0, -1)
		self.assertAlmostEqualTup((-1, 0), self.deg45_wall.get_resultant_vel(vel))
		
		vel = (1, -1)
		self.assertAlmostEqualTup((-1, 1), self.deg45_wall.get_resultant_vel(vel))

	def testWallBuilder(self):
		wall_builder = wall.WallBuilder((0, 50), (100, 150), (200, 250))
		walls = wall_builder.build()

		expected_walls = [wall.Wall((0, 50), (100, 150)), wall.Wall((100, 150), (200, 250)), wall.Wall((200, 250), (0, 50))]

		self.assertEqual(expected_walls, walls)
		
	def assertAlmostEqualTup(self, expected, actual):
		self.assertAlmostEqual(expected[0], actual[0], places=7)
		self.assertAlmostEqual(expected[1], actual[1], places=7)
		
		