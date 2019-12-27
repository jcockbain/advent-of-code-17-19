import unittest

import day_02


class TestSum(unittest.TestCase):
    def test_part_1_1(self):
        data = [1, 0, 0, 0, 99]
        result = day_02.run_comp(data)
        self.assertEqual(result, [2, 0, 0, 0, 99])

    def test_part_1_2(self):
        data = [2, 3, 0, 3, 99]
        result = day_02.run_comp(data)
        self.assertEqual(result, [2, 3, 0, 6, 99])

    def test_part_1_3(self):
        data = [2, 4, 4, 5, 99, 0]
        result = day_02.run_comp(data)
        self.assertEqual(result, [2, 4, 4, 5, 99, 9801])

    def test_part_1_4(self):
        data = [1, 1, 1, 4, 99, 5, 6, 0, 99]
        result = day_02.run_comp(data)
        self.assertEqual(result, [30, 1, 1, 4, 2, 5, 6, 0, 99])


if __name__ == '__main__':
    unittest.main()
