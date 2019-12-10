import unittest

import answer


class TestSum(unittest.TestCase):
    def test_part_1(self):
        pixels = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2]

        got = answer.part_1(pixels, 3, 2)
        want = 1
        self.assertEqual(got, want)


if __name__ == '__main__':
    unittest.main()
