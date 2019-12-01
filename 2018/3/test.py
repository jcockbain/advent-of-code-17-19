import unittest

import answer


class TestSum(unittest.TestCase):
    def test_part_1_1(self):
        data = ['#1 @ 2,2: 2x2', '#2 @ 1,1: 4x4']
        result = answer.part_1(data)
        self.assertEqual(result, 4)

    def test_part_1_2(self):
        data = ['#1 @ 3,3: 1x1', '#2 @ 3,3: 2x2']
        result = answer.part_1(data)
        self.assertEqual(result, 1)

    def test_part_2_1(self):
        data = ['#1 @ 1,1: 1x1', '#2 @ 3,3: 2x2', '#3 @ 3,3: 2x1']
        result = answer.part_1(data)
        self.assertEqual(result, 1)

    def test_part_2_2(self):
        data = ['#1 @ 3,3: 3x3', '#2 @ 5,5: 2x2', '#2 @ 3,2: 2x2']
        result = answer.part_1(data)
        self.assertEqual(result, 2)


if __name__ == '__main__':
    unittest.main()
