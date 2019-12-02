import unittest

import answer


class TestSum(unittest.TestCase):
    def test_part_1_1(self):
        data = [('A', 'B'), ('B', 'C'), ('C', 'D')]
        result = answer.part_1(data)
        self.assertEqual(result, 'ABCD')

    def test_part_1_2(self):
        data = [('A', 'C'), ('C', 'B'), ('B', 'E')]
        result = answer.part_1(data)
        self.assertEqual(result, 'ACBE')


if __name__ == '__main__':
    unittest.main()
