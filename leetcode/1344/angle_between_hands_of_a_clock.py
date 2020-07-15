#!/usr/bin/env python3
"""

"""
import unittest


class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        angle = abs(
            (hour * 30 % 360 + (minutes / 60) * 30) - (minutes / 5) * 30)
        return min(360 - angle, angle)


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_angleClock(self):

        hour, minutes = 12, 30
        self.assertEqual(165.00000, self.solution.angleClock(hour, minutes))

        hour, minutes = 3, 30
        self.assertEqual(75.00000, self.solution.angleClock(hour, minutes))

        hour, minutes = 1, 1
        self.assertEqual(24.50000, self.solution.angleClock(hour, minutes))

        hour, minutes = 12, 0
        self.assertEqual(0.00000, self.solution.angleClock(hour, minutes))

        hour, minutes = 3, 0
        self.assertEqual(90.00000, self.solution.angleClock(hour, minutes))

        hour, minutes = 2, 1
        self.assertEqual(54.50000, self.solution.angleClock(hour, minutes))

        hour, minutes = 11, 0
        self.assertEqual(30.00000, self.solution.angleClock(hour, minutes))

        hour, minutes = 12, 31
        self.assertEqual(170.50000, self.solution.angleClock(hour, minutes))

        hour, minutes = 2, 20
        self.assertEqual(50.00000, self.solution.angleClock(hour, minutes))

        hour, minutes = 9, 2
        self.assertEqual(101.00000, self.solution.angleClock(hour, minutes))

        hour, minutes = 12, 29
        self.assertEqual(159.50000, self.solution.angleClock(hour, minutes))


if __name__ == "__main__":
    unittest.main()
