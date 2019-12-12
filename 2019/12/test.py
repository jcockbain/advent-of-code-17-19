import unittest

import answer


class TestSum(unittest.TestCase):
    def test_part_1_1(self):
        with open('test1.in', 'r') as f:
            file = f.read()
        inp = file.split('\n')
        energy = answer.p1(inp, 10)
        want = 179
        self.assertEqual(energy, want)

    def test_part_1_2(self):
        with open('test2.in', 'r') as f:
            file = f.read()
        inp = file.split('\n')
        energy = answer.p1(inp, 100)
        want = 1940
        self.assertEqual(energy, want)

    def test_part_2_1(self):
        with open('test2.in', 'r') as f:
            file = f.read()
        inp = file.split('\n')
        steps = answer.p2(inp)
        want = 4686774924
        self.assertEqual(steps, want)


if __name__ == '__main__':
    unittest.main()
