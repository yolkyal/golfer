import unittest
import hole
from unittest import mock


class TestHole(unittest.TestCase):
	def setUp(self):
		self.ball = mock.Mock()
		self.ball_start_pos = (0, 0)
		self.golfer_start_direction = 0
		self.hole_pos = (0, 0)
		self.wall = mock.Mock()
		self.wall.is_collision.return_value = False
		self.hole = hole.Hole(self.ball_start_pos, self.hole_pos, self.golfer_start_direction, [self.wall])

	def testUpdate(self):
		self.ball.pos = (1, 2)
		self.ball.vel = (3, 4)
		time_delta = 2

		expected_ball_pos = (self.ball.pos[0] + self.ball.vel[0] * time_delta, self.ball.pos[1] + self.ball.vel[1] * time_delta)
		expected_ball_vel = (self.ball.vel[0] * hole.DEFAULT_SURFACE_DRAG, self.ball.vel[1] * hole.DEFAULT_SURFACE_DRAG)

		self.hole.update(self.ball, time_delta)

		self.assertEqual(expected_ball_pos, self.ball.pos)
		self.assertEqual(expected_ball_vel, self.ball.vel)
		
	@mock.patch('commons.get_dist')
	def testUpdateWithWallCollision(self, mock_get_dist):
		self.wall.is_collision.side_effect = [True, False]
		mock_get_dist.return_value = 1
		orig_ball_pos = (1, 2)
		self.ball.pos = orig_ball_pos
		self.ball.vel = (3, 4)
		
		next_ball_pos = (self.ball.pos[0] + self.ball.vel[0], self.ball.pos[1] + self.ball.vel[1])
		next_ball_vel = (3 * hole.DEFAULT_SURFACE_DRAG, 4 * hole.DEFAULT_SURFACE_DRAG)
		
		self.hole.update(self.ball)
		
		self.wall.get_resultant_vel.assert_called_once_with(next_ball_vel)
		self.wall.get_resultant_pos.assert_called_once_with(next_ball_pos)
		self.assertEqual(self.ball.vel, self.wall.get_resultant_vel(next_ball_vel))
		self.assertEqual(self.ball.pos, self.wall.get_resultant_pos(next_ball_pos))
		mock_get_dist.assert_called_once_with(orig_ball_pos, self.wall.get_collision_pt((1, 2), next_ball_pos))
		
	@mock.patch('commons.get_dist')
	def testUpdateWithDoubleWallCollision(self, mock_get_dist):
		mock_get_dist.return_value = 1
		wall1 = mock.Mock()
		wall2 = mock.Mock()
		wall1.is_collision.side_effect = [True, False, False]
		wall2.is_collision.side_effect = [False, True, False]
		orig_ball_pos = (1, 2)
		self.ball.pos = orig_ball_pos
		self.ball.vel = (3, 4)
		
		self.hole.walls = [wall1, wall2]
		
		next_ball_pos = (self.ball.pos[0] + self.ball.vel[0], self.ball.pos[1] + self.ball.vel[1])
		next_ball_vel = (3 * hole.DEFAULT_SURFACE_DRAG, 4 * hole.DEFAULT_SURFACE_DRAG)
		
		self.hole.update(self.ball)
		
		wall1_collision_pt = wall1.get_collision_pt(orig_ball_pos, next_ball_pos)
		wall1_resultant_pos = wall1.get_resultant_pos(next_ball_pos)
		wall2_collision_pt = wall2.get_collision_pt(wall1_collision_pt, wall1_resultant_pos)
		wall2_resultant_pos = wall2.get_resultant_pos(wall1_resultant_pos)
		
		is_collision_expected_calls = [mock.call(orig_ball_pos, next_ball_pos), mock.call(wall1_collision_pt, wall1_resultant_pos), mock.call(wall2_collision_pt, wall2_resultant_pos)]
		
		self.assertEqual(is_collision_expected_calls, wall1.is_collision.call_args_list)
		self.assertEqual(is_collision_expected_calls, wall2.is_collision.call_args_list)

	def testIsComplete(self):
		self.ball.pos = (0, hole.DEFAULT_HOLE_RADIUS)

		self.assertTrue(self.hole.is_complete(self.ball))