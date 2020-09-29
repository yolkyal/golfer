import unittest
import commons

class TestCommons(unittest.TestCase):
	def testGetDist(self):
		pt1 = (0, 0)
		pt2 = (3, 4)
		
		self.assertEqual(5, commons.get_dist(pt1, pt2))