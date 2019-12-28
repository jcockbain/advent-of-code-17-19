import unittest
import os

import day_13


class TestSum(unittest.TestCase):

    def test_q_1(self):
        filename = os.path.splitext(os.path.dirname(__file__))[
            0] + '/inputs/13.in'
        with open(filename) as f:
            data = list(map(int, f.read().split(',')))
        result = day_13.p1(data)
        self.assertEqual(result, 306)

    def test_q_2(self):
        filename = os.path.splitext(os.path.dirname(__file__))[
            0] + '/inputs/13.in'
        with open(filename) as f:
            data = list(map(int, f.read().split(',')))
        result = day_13.p2(data)
        self.assertEqual(result, 15328)


if __name__ == '__main__':
    unittest.main()
