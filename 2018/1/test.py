import unittest

import answer


class TestSum(unittest.TestCase):
    def test_part_1_1(self):
        data = [1, 2, 3]
        result = answer.part_1(data)
        self.assertEqual(result, 6)

    def test_part_1_2(self):
        data = [1, 2, 3, -1, -4]
        result = answer.part_1(data)
        self.assertEqual(result, 1)

    def test_part_2_1(self):
        data = [1, 2, -3, -1, 1]
        result = answer.part_2(data)
        self.assertEqual(result, 0)

    def test_part_2_2(self):
        data = [1, 2, 3, -6]
        result = answer.part_2(data)
        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()
