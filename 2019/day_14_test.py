import unittest

import day_14


class TestSum(unittest.TestCase):
    def test_part_1_1(self):
        inp = day_14.get_input('inputs/14_test_1.in')
        ore = day_14.part1(inp)
        want = 165
        self.assertEqual(ore, want)

    def test_part_1_2(self):
        inp = day_14.get_input('inputs/14_test_2.in')
        ore = day_14.part1(inp)
        want = 13312
        self.assertEqual(ore, want)

    def test_part_1_3(self):
        inp = day_14.get_input('inputs/14_test_3.in')
        ore = day_14.part1(inp)
        want = 180697
        self.assertEqual(ore, want)

    def test_part_1_4(self):
        inp = day_14.get_input('inputs/14_test_4.in')
        ore = day_14.part1(inp)
        want = 2210736
        self.assertEqual(ore, want)


if __name__ == '__main__':
    unittest.main()
