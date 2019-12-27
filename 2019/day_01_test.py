import unittest

import day_01


class TestSum(unittest.TestCase):
    def test_part_1_1(self):
        data = [14, 12]
        result = day_01.part_1(data)
        self.assertEqual(result, 4)

    def test_part_1_2(self):
        data = [17, 18, 19]
        result = day_01.part_1(data)
        self.assertEqual(result, 11)

    def test_part_2_1(self):
        data = [18, 21]
        result = day_01.part_2(data)
        self.assertEqual(result, 9)

    def test_part_2_2(self):
        data = [14, 13]
        result = day_01.part_2(data)
        self.assertEqual(result, 4)


if __name__ == '__main__':
    unittest.main()
