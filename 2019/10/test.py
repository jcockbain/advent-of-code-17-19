import unittest

import answer


class TestSum(unittest.TestCase):
    def test_part_1_1(self):
        with open('test1.in', 'r') as f:
            file = f.read()
        inp = file.split('\n')
        pos, asteroids_seen = answer.p1(inp)
        want = 8
        self.assertEqual(pos, (3, 4))
        self.assertEqual(asteroids_seen, want)

    def test_part_1_2(self):
        with open('test2.in', 'r') as f:
            file = f.read()
        inp = file.split('\n')
        pos, asteroids_seen = answer.p1(inp)
        want = 33
        self.assertEqual(pos, (5, 8))
        self.assertEqual(asteroids_seen, want)

    def test_part_1_3(self):
        with open('test3.in', 'r') as f:
            file = f.read()
        inp = file.split('\n')
        pos, asteroids_seen = answer.p1(inp)
        want = 35
        self.assertEqual(pos, (1, 2))
        self.assertEqual(asteroids_seen, want)

    def test_part_1_4(self):
        with open('test4.in', 'r') as f:
            file = f.read()
        inp = file.split('\n')
        pos, asteroids_seen = answer.p1(inp)
        want = 41
        self.assertEqual(pos, (6, 3))
        self.assertEqual(asteroids_seen, want)

    def test_part_1_5(self):
        with open('test5.in', 'r') as f:
            file = f.read()
        inp = file.split('\n')
        pos, asteroids_seen = answer.p1(inp)
        want = 210
        self.assertEqual(pos, (11, 13))
        self.assertEqual(asteroids_seen, want)

    def test_part_2_1(self):
        with open('test5.in', 'r') as f:
            file = f.read()
        inp = file.split('\n')
        asteroids_seen = answer.p2(inp, (11, 13))
        want = 802
        self.assertEqual(asteroids_seen, want)


if __name__ == '__main__':
    unittest.main()
