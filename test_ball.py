import unittest
import ball
from math import cos, sin


class TestBall(unittest.TestCase):
	def setUp(self):
		self.pos = (0, 0)
		self.colour = (220, 220, 220)
		self.ball = ball.Ball(self.pos, self.colour)

	def testApplyForce(self):
		force_mag = 1
		force_dir = 1

		self.ball.apply_force(force_mag, force_dir)

		self.assertEqual((cos(force_dir) * force_mag, sin(force_dir) * force_mag), self.ball.vel)

	def testIsStationary(self):
		self.ball.vel = (1, 1)
		self.assertFalse(self.ball.is_stationary())

		self.ball.vel = (0, 0)
		self.assertTrue(self.ball.is_stationary())