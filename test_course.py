import unittest


class TestCourse(unittest.TestCase):
	def setUp(self):
		self.hole = mock.Mock()
		self.course = course.Course([self.hole])