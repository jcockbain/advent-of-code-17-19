import unittest
import os

import day_21


class TestSum(unittest.TestCase):

    def test_q_1(self):
        filename = os.path.splitext(os.path.dirname(__file__))[
            0] + '/inputs/21.in'
        with open(filename) as f:
            inp = f.read().strip()
        data = list(map(int, inp.split(',')))
        result = day_21.p1(data)
        self.assertEqual(result, 19354890)

    def test_q_2(self):
        filename = os.path.splitext(os.path.dirname(__file__))[
            0] + '/inputs/21.in'
        with open(filename) as f:
            inp = f.read().strip()
        data = list(map(int, inp.split(',')))
        result = day_21.p2(data)
        self.assertEqual(result, 1140664209)


if __name__ == '__main__':
    unittest.main()
