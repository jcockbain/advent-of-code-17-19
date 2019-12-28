import unittest
import os

import day_15


class TestSum(unittest.TestCase):

    def test_q_1(self):
        filename = os.path.splitext(os.path.dirname(__file__))[
            0] + '/inputs/15.in'
        with open(filename) as f:
            data = list(map(int, f.read().split(',')))
        result = day_15.p1(data)
        self.assertEqual(result, 424)


if __name__ == '__main__':
    unittest.main()
