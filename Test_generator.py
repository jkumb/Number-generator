'''
Test with a valid input (example: 35)
Test with a negative input (example: -5)
Test with zero as input (example: 0)
Test with no multiples of 5 or 7 (example: 25)
Test with a large input (example: 500)

'''

import unittest
from generator import num_generator

class TestNumGenerator(unittest.TestCase):
    def test_valid_input(self):
        expected_output = [0, 35]
        result = list(num_generator(35))
        self.assertEqual(result, expected_output)

    def test_negative_input(self):
        expected_output = []
        result = list(num_generator(-5))
        self.assertEqual(result, expected_output)

    def test_zero_input(self):
        expected_output = [0]
        result = list(num_generator(0))
        self.assertEqual(result, expected_output)

    def test_multiples_num(self):
        expected_output = [0]
        result = list(num_generator(25))
        self.assertEqual(result, expected_output)

    def test_max_input(self):
        expected_output = [0, 35, 70, 105, 140, 175, 210, 245, 280, 315, 350, 385, 420, 455, 490]
        result = list(num_generator(500))
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()
