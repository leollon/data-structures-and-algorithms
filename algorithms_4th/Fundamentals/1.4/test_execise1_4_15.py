import unittest

from execise1_4_15 import ThreeSumFaster


class TestThreeSumFaster(unittest.TestCase):

    def test_three_sum_faster(self):
        s = ThreeSumFaster()

        array, target = [-1, 0, 1, 2, -2, 3, -4, 5, -5, 7, 3], 0
        self.assertEqual(
            s.three_sum_faster(array, target),
            [
                (-5, 2, 3), (-2, 0, 2), (-4, 1, 3), (-4, -1, 5),
                (-1, 0, 1), (-5, -2, 7), (-2, -1, 3), (-5, 0, 5)
            ]
        )

        array, target = [2, 1, -1, 5, 9, 7, 2, 0, 6, -1, -2, -4, 11, 10, -3], 5
        self.assertEqual(
            s.three_sum_faster(array, target),
            [
                (-1, 0, 6), (-1, 1, 5), (-4, 2, 7), (-3, 1, 7), (-3, 2, 6),
                (-2, 2, 5), (1, 2, 2), (-2, 1, 6), (-4, 0, 9), (-3, -1, 9),
                (-3, -2, 10), (-1, -1, 7), (-4, -2, 11), (-2, 0, 7), (-4, -1, 10)
            ]
        )

        array, target = [8, 3, 2, 4, 1, 0, -1, -2, -5, 9, 11, 0], 6
        self.assertEqual(
            s.three_sum_faster(array, target),
            [
                (-5, 3, 8), (-1, 3, 4), (1, 2, 3), (-2, -1, 9),
                (-2, 0, 8), (-5, 2, 9), (-5, 0, 11), (0, 2, 4)
            ]
        )

        array = [], 0
        self.assertEqual(s.three_sum_faster(array, target), [])


if __name__ == "__main__":
    unittest.main()
