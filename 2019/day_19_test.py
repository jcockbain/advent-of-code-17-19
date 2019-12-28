import unittest
import os

import day_19


class TestSum(unittest.TestCase):

    def test_q_1(self):
        filename = os.path.splitext(os.path.dirname(__file__))[
            0] + 'inputs/19.in'
        with open(filename) as f:
            data = list(map(int, f.read().split(',')))
        result = day_19.p1(data)
        self.assertEqual(result, 183)

    def test_q_2(self):
        filename = os.path.splitext(os.path.dirname(__file__))[
            0] + 'inputs/19.in'
        with open(filename) as f:
            data = list(map(int, f.read().split(',')))
        result = day_19.p2(data)
        self.assertEqual(result, 11221248)


if __name__ == '__main__':
    unittest.main()
