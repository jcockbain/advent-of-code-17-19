import unittest

import answer


class TestSum(unittest.TestCase):
    def test_part_1(self):
        data = [["COM", "B"], ["B", "C"], ["C", "D"], ["D", "E"], ["E", "F"],
                ["B", "G"], ["G", "H"], ["D", "I"], ["E", "J"], ["J", "K"], ["K", "L"]]
        result = answer.part_1(data)
        self.assertEqual(result, 42)


if __name__ == '__main__':
    unittest.main()
