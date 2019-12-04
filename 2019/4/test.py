import unittest

import answer


class TestSum(unittest.TestCase):
    def test_is_password_1_1(self):
        result = answer.is_password_1(111111)
        self.assertEqual(result, True)

    def test_is_password_1_2(self):
        result = answer.is_password_1(223450)
        self.assertEqual(result, False)

    def test_is_password_1_1(self):
        result = answer.is_password_2(123444)
        self.assertEqual(result, False)

    def test_is_password_1_2(self):
        result = answer.is_password_2(111122)
        self.assertEqual(result, True)


if __name__ == '__main__':
    unittest.main()
