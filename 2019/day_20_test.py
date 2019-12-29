import unittest
import os

import day_20


class TestSum(unittest.TestCase):

    def test_q_1(self):
        filename = os.path.splitext(os.path.dirname(__file__))[
            0] + '/inputs/20.in'
        with open(filename) as f:
            inp = f.read().split('\n')
        result = day_20.p1(inp)
        self.assertEqual(result, 556)

    def test_q_2(self):
        filename = os.path.splitext(os.path.dirname(__file__))[
            0] + '/inputs/20.in'
        with open(filename) as f:
            inp = f.read().split('\n')
        result = day_20.p2(inp)
        self.assertEqual(result, 6532)


if __name__ == '__main__':
    unittest.main()
