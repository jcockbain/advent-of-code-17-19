import unittest
import os

import day_05


class TestSum(unittest.TestCase):
    def test_q_2(self):
        filename = os.path.splitext(os.path.dirname(__file__))[
            0] + '/inputs/05.in'
        with open(filename) as f:
            data = list(map(int, f.read().split(',')))
        result = day_05.p2(data)
        self.assertEqual(result, 8834787)


if __name__ == '__main__':
    unittest.main()
