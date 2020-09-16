import unittest
import course_drawer
from unittest import mock


class TestCourseDrawer(unittest.TestCase):
	def setUp(self):
		self.d_surf = mock.Mock()
		self.course = mock.Mock()
		self.course_drawer = course_drawer.CourseDrawer()

	@mock.patch('pygame.draw.circle')
	def testDraw(self, mock_draw_circle):
		self.course_drawer.draw(self.d_surf, self.course)

		mock_draw_circle.assert_called_once_with(self.d_surf, course_drawer.DEFAULT_HOLE_COLOUR, self.course.hole_pos, course_drawer.DEFAULT_HOLE_RADIUS)