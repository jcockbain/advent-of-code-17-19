import unittest

import answer


class TestSum(unittest.TestCase):
    def test_part_1_1(self):
        data = ['aa', 'bbb']
        result = answer.part_1(data)
        self.assertEqual(result, 1)

    def test_part_1_2(self):
        data = ['aabbb', 'aa', 'bb', 'ab', 'cc']
        result = answer.part_1(data)
        self.assertEqual(result, 4)

    def test_part_2_1(self):
        data = ['aabbb', 'aaaaa', 'aabbc', 'abcde', 'cceds']
        result = answer.part_2(data)
        self.assertEqual(result, 'aabb')

    def test_part_2_2(self):
        data = ['bbcds', 'bdhsa', 'skajc', 'wksmc', 'abcds']
        result = answer.part_2(data)
        self.assertEqual(result, 'bcds')


if __name__ == '__main__':
    unittest.main()
