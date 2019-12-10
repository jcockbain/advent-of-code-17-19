import unittest

import answer


class TestSum(unittest.TestCase):
    def test_part_1_1(self):
        data = [14, 12]
        result = answer.part_1(data)
        self.assertEqual(result, 4)

    def test_part_1_2(self):
        data = [17, 18, 19]
        result = answer.part_1(data)
        self.assertEqual(result, 11)

    def test_part_2_1(self):
        data = [18, 21]
        result = answer.part_2(data)
        self.assertEqual(result, 9)

    def test_part_2_2(self):
        data = [14, 13]
        result = answer.part_2(data)
        self.assertEqual(result, 4)


if __name__ == '__main__':
    unittest.main()
