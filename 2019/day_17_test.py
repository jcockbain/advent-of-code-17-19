import unittest
import os

import day_17


class TestSum(unittest.TestCase):

    def test_q_1(self):
        filename = os.path.splitext(os.path.dirname(__file__))[
            0] + 'inputs/17.in'
        with open(filename) as f:
            data = list(map(int, f.read().split(',')))
        result = day_17.p1(data)
        self.assertEqual(result, 2804)


if __name__ == '__main__':
    unittest.main()
