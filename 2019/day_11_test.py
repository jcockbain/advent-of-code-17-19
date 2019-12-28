import unittest
import os

import day_11


class TestSum(unittest.TestCase):

    def test_q_1(self):
        filename = os.path.splitext(os.path.dirname(__file__))[
            0] + 'inputs/11.in'
        with open(filename) as f:
            data = list(map(int, f.read().split(',')))
        result = day_11.run_robot(data, 0)
        self.assertEqual(len(result), 2268)


if __name__ == '__main__':
    unittest.main()
