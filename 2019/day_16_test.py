import unittest

import day_16


class TestSum(unittest.TestCase):
    def test_part_1_1(self):
        inp = "80871224585914546619083218645595"
        ans = day_16.p1(inp)
        want = 24176176
        self.assertEqual(ans, want)

    def test_part_1_2(self):
        inp = "19617804207202209144916044189917"
        ans = day_16.p1(inp)
        want = 73745418
        self.assertEqual(ans, want)

    def test_part_1_3(self):
        inp = "69317163492948606335995924319873"
        ans = day_16.p1(inp)
        want = 52432133
        self.assertEqual(ans, want)

    # def test_part_2_1(self):
    #     inp = "03036732577212944063491565474664"
    #     ans = day_16.p2(inp)
    #     want = 84462026
    #     self.assertEqual(ans, want)

    # def test_part_2_2(self):
    #     inp = "02935109699940807407585447034323"
    #     ans = day_16.p2(inp)
    #     want = 78725270
    #     self.assertEqual(ans, want)

    # def test_part_2_3(self):
    #     inp = "03081770884921959731165446850517"
    #     ans = day_16.p2(inp)
    #     want = 53553731
    #     self.assertEqual(ans, want)


if __name__ == '__main__':
    unittest.main()
