import unittest
import cube_volume
import average
import name_gen

class test_hw4(unittest.TestCase):

	def test_cube_volume(self):
		self.assertEqual(cube_volume.volume(.5), .125)
		self.assertEqual(cube_volume.volume(5), 125)
		self.assertEqual(cube_volume.volume(-2), 0)

	def test_average(self):
		self.assertEqual(average.average([-0.5, -0.5]), -0.5)
		self.assertEqual(average.average([-0.5, 0.5]), 0)
		self.assertEqual(average.average([1,2,3]), 2)
		self.assertEqual(average.average([2.1,2.5,3.8]), 2.8)
		self.assertEqual(average.average([]), 0)
		self.assertEqual(average.average(0), None)

	def test_name_gen(self):
		self.assertEqual(name_gen.generate_name("", "last"), "last")
		self.assertEqual(name_gen.generate_name("first", ""), "first")
		self.assertEqual(name_gen.generate_name("123", ".123"), "123.123")


if __name__ == '__main__':
	unittest.main(verbosity=2)
