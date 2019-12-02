import unittest

import answer


class TestSum(unittest.TestCase):
    def test_part_1_1(self):
        data = [(1, 2), (3, 2), (3, 3), (2, 2)]
        result = answer.part_1(data)
        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()
