import unittest
import os

import day_09


class TestSum(unittest.TestCase):

    def test_q_1(self):
        filename = os.path.splitext(os.path.dirname(__file__))[
            0] + '/inputs/09.in'
        with open(filename) as f:
            data = list(map(int, f.read().split(',')))
        result = day_09.run(data, [1])
        self.assertEqual(result, 2594708277)

    def test_q_2(self):
        filename = os.path.splitext(os.path.dirname(__file__))[
            0] + '/inputs/09.in'
        with open(filename) as f:
            data = list(map(int, f.read().split(',')))
        result = day_09.run(data, [2])
        self.assertEqual(result, 87721)


if __name__ == '__main__':
    unittest.main()
