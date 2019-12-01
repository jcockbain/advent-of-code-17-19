import unittest

import answer


class TestSum(unittest.TestCase):
    def test_part_1_1(self):
        data = 'Aabcd'
        result = answer.part_1(data)
        self.assertEqual(result, 3)

    def test_part_1_1(self):
        data = 'abcdEe'
        result = answer.part_1(data)
        self.assertEqual(result, 4)

    def test_part_2_1(self):
        data = 'abcBEef'
        result = answer.part_2(data)
        self.assertEqual(result, 2)

    def test_part_2_2(self):
        data = 'acAdEg'
        result = answer.part_2(data)
        self.assertEqual(result, 3)


if __name__ == '__main__':
    unittest.main()
