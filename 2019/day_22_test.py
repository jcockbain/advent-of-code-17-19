import unittest
import os

import day_22


class TestSum(unittest.TestCase):

    def test_deal_new_stack(self):
        result = day_22.deal_new_stack([1, 2, 3, 4])
        self.assertEqual(result, [4, 3, 2, 1])

    def test_cut(self):
        result = day_22.cut([1, 2, 3, 4], 2)
        self.assertEqual(result, [3, 4, 1, 2])

    def test_negative_cut(self):
        result = day_22.cut([1, 2, 3, 4], -1)
        self.assertEqual(result, [4, 1, 2, 3])

    def test_deal_inc(self):
        result = day_22.deal_inc([1, 2, 3, 4, 5], 2)
        self.assertEqual(result, [1, 4, 2, 5, 3])

    def test_deal_inc_2(self):
        result = day_22.deal_inc([1, 2, 3, 4, 5], 1)
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_process_instruction_1(self):
        test = "cut 1727"
        code, value = day_22.process_instruction(test)
        self.assertEqual(code, "cut")
        self.assertEqual(value, 1727)

    def test_process_instruction_2(self):
        test = "cut -1727"
        code, value = day_22.process_instruction(test)
        self.assertEqual(code, "cut")
        self.assertEqual(value, -1727)

    def test_process_instruction_3(self):
        test = "increment 1727"
        code, value = day_22.process_instruction(test)
        self.assertEqual(code, "increment")
        self.assertEqual(value, 1727)

    def test_process_instruction_4(self):
        test = "deal into new stack"
        code, value = day_22.process_instruction(test)
        self.assertEqual(code, "new_stack")
        self.assertEqual(value, None)

    def test_1(self):
        with open("inputs/22_test_1.in", "r") as f:
            instructions = f.read().split('\n')
        result = day_22.p1(instructions, 10)
        self.assertEqual(result, [0, 3, 6, 9, 2, 5, 8, 1, 4, 7])

    def test_2(self):
        with open("inputs/22_test_2.in", "r") as f:
            instructions = f.read().split('\n')
        result = day_22.p1(instructions, 10)
        self.assertEqual(result, [3, 0, 7, 4, 1, 8, 5, 2, 9, 6])

    def test_3(self):
        with open("inputs/22_test_3.in", "r") as f:
            instructions = f.read().split('\n')
        result = day_22.p1(instructions, 10)
        self.assertEqual(result, [6, 3, 0, 7, 4, 1, 8, 5, 2, 9])

    def test_4(self):
        with open("inputs/22_test_4.in", "r") as f:
            instructions = f.read().split('\n')
        result = day_22.p1(instructions, 10)
        self.assertEqual(result, [9, 2, 5, 8, 1, 4, 7, 0, 3, 6])


if __name__ == '__main__':
    unittest.main()
