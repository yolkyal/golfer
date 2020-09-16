import unittest
import time, datetime
import golfer
from unittest import mock


class TestGolfer(unittest.TestCase):
	def setUp(self):
		self.ball = mock.Mock()
		self.ball.is_stationary.return_value = True
		self.start_direction = 0
		self.golfer = golfer.Golfer(self.ball, self.start_direction)

	def testTurnLeft(self):
		self.golfer.start_turn_left()
		self.golfer.update()
		self.golfer.end_turn_left()
		self.golfer.update()

		self.assertEqual(self.start_direction - golfer.TURN_ANGLE, self.golfer.direction)

	def testTurnRight(self):
		self.golfer.start_turn_right()
		self.golfer.update()
		self.golfer.end_turn_right()
		self.golfer.update()

		self.assertEqual(golfer.TURN_ANGLE, self.golfer.direction)

	# uses internal variable because datetime.datetime.now() cannot be patched
	def testGetCompletedSwingTime(self):
		self.golfer.start_swing_time = datetime.datetime(2020, 1, 1, 10, 0, 0, 500000)
		self.golfer.end_swing_time = datetime.datetime(2020, 1, 1, 10, 0, 2, 0)

		self.assertEqual(1.5, self.golfer.get_completed_swing_time())

	def testSwing(self):
		direction = 1
		self.golfer.direction = direction

		self.golfer.start_swing()
		time.sleep(1)
		self.golfer.end_swing()
		swing_time = self.golfer.get_completed_swing_time() # required because datetime.datetime.now() cannot be patched
		self.golfer.update()

		self.ball.apply_force.assert_called_once_with(swing_time * golfer.SWING_FORCE_TIME_MULTIPLIER, direction)

	def testSwingLimit(self):
		direction = 1
		self.golfer.direction = direction

		self.golfer.start_swing()
		time.sleep(golfer.SWING_TIME_LIMIT.seconds + 1)
		self.golfer.update()

		self.ball.apply_force.assert_called_once_with((golfer.SWING_TIME_LIMIT.seconds + golfer.SWING_TIME_LIMIT.microseconds / 1000000) * golfer.SWING_FORCE_TIME_MULTIPLIER, direction)

	def testSwingWhileBallMoving(self):
		self.ball.is_stationary.return_value = False

		self.golfer.start_swing()
		self.golfer.end_swing()
		self.golfer.update()

		self.ball.apply_force.assert_not_called()

	def testTurnWhileSwingActive(self):
		self.golfer.start_swing()
		self.golfer.start_turn_left()
		self.golfer.update()

		self.assertEqual(self.start_direction, self.golfer.direction)

	def testTurnWhileBallMoving(self):
		self.ball.is_stationary.return_value = False

		self.golfer.start_turn_left()
		self.golfer.update()

		self.assertEqual(self.start_direction, self.golfer.direction)