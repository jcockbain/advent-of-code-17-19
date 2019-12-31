import unittest
import os

import day_24


class TestSum(unittest.TestCase):
    def test_get_world_1(self):
        data = ["#.", ".#"]
        expected = {(0, 0): "#",
                    (1, 0): ".",
                    (0, 1): ".",
                    (1, 1): "#"
                    }
        actual = day_24.get_grid(data)
        self.assertEqual(actual, expected)

    def test_get_world_2(self):
        data = ["#", "."]
        expected = {(0, 0): "#",
                    (0, 1): "."
                    }
        actual = day_24.get_grid(data)
        self.assertEqual(actual, expected)

    def test_get_nbs(self):
        expected = [(1, 0), (2, 1), (1, 2), (0, 1)]
        actual = day_24.get_nbs((1, 1))
        self.assertListEqual(expected, actual)

    def test_is_alive(self):
        self.assertEqual(day_24.is_alive("#"), True)
        self.assertEqual(day_24.is_alive("."), False)

    def test_print_world(self):
        data = {(0, 0): "#",
                (0, 1): "."
                }
        expected = "#."
        actual = day_24.print_world(data)
        self.assertEqual(actual, expected)

    def test_print_world_2(self):
        data = {(0, 0): "#",
                (1, 0): ".",
                (0, 1): ".",
                (1, 1): "#"
                }
        expected = "#.\n.#"
        actual = day_24.print_world(data)
        self.assertEqual(actual, expected)

    def test_get_biodiversity_rating(self):
        data = {(0, 0): "#",
                (1, 0): ".",
                (0, 1): ".",
                (1, 1): "#"
                }
        actual = day_24.get_biodiversity_rating(data)
        self.assertEqual(actual, 9)

    def test_iter_1(self):
        with open("inputs/24_test_1.in", "r") as f:
            data = f.read().split("\n")
        grid = day_24.get_grid(data)
        result = day_24.iter(grid)
        printed = day_24.print_world(result)
        with open("inputs/24_test_1_expected.in", "r") as f:
            expected = f.read()
        self.assertEqual(printed, expected)

    def test_iter_2(self):
        with open("inputs/24_test_1.in", "r") as f:
            data = f.read().split("\n")
        grid = day_24.get_grid(data)
        for _ in range(4):
            grid = day_24.iter(grid)
        printed = day_24.print_world(grid)
        with open("inputs/24_test_4_expected.in", "r") as f:
            expected = f.read()
        self.assertEqual(printed, expected)


if __name__ == "__main__":
    unittest.main()
