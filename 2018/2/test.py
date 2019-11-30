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


if __name__ == '__main__':
    unittest.main()
