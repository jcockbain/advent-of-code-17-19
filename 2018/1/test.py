import unittest

import answer


class TestSum(unittest.TestCase):
    def test_list_int_1(self):
        data = [1, 2, 3]
        result = answer.sum_frequency(data)
        self.assertEqual(result, 6)

    def test_list_int_2(self):
        data = [1, 2, 3, -1, -4]
        result = answer.sum_frequency(data)
        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()
