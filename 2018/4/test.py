import unittest

import answer


class TestSum(unittest.TestCase):
    def test_part_1_1(self):
        data = ['[1518-06-12 00:00] Guard #1 begins shift',
                '[1518-06-12 00:10] falls asleep',
                '[1518-06-12 00:20] wakes up',
                '[1518-06-13 00:00] Guard #1 begins shift',
                '[1518-06-13 00:19] falls asleep',
                '[1518-06-13 00:30] wakes up',
                ]
        result = answer.part_1(data)
        self.assertEqual(result, 19)

    def test_part_2_1(self):
        data = ['[1518-06-12 00:00] Guard #1 begins shift',
                '[1518-06-12 00:10] falls asleep',
                '[1518-06-12 00:20] wakes up',
                '[1518-06-13 00:00] Guard #1 begins shift',
                '[1518-06-13 00:19] falls asleep',
                '[1518-06-13 00:30] wakes up',
                '[1518-06-12 00:00] Guard #2 begins shift',
                '[1518-06-12 00:10] falls asleep',
                '[1518-06-12 00:20] wakes up',
                '[1518-06-13 00:00] Guard #2 begins shift',
                '[1518-06-13 00:19] falls asleep',
                '[1518-06-13 00:30] wakes up',
                '[1518-06-14 00:00] Guard #2 begins shift',
                '[1518-06-14 00:19] falls asleep',
                '[1518-06-14 00:30] wakes up',

                ]
        result = answer.part_1(data)
        self.assertEqual(result, 38)


if __name__ == '__main__':
    unittest.main()
