"""Merge Intervals
Given a collection of intervals, merge all overlapping intervals.

Example 1:

    Input: [[1,3],[2,6],[8,10],[15,18]]
    Output: [[1,6],[8,10],[15,18]]
    Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:

    Input: [[1,4],[4,5]]
    Output: [[1,5]]
    Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""


# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def merge(self, intervals):
        """
        :type: List[Interval]
        :rtype: List[Interval]
        asume that:
            c1 = (a1, b1)
            c2 = (a2, b2)

        Examples

            >>> s = Solution()
            >>> def create(array):
            ...     result = []
            ...     for val in array:
            ...         result.append(Interval(*val))
            ...     return result

            >>> nums = [[1, 3], [2, 6], [8, 10], [15, 18]]
            >>> intervals = create(nums)
            >>> result = s.merge(intervals)
            >>> s.show(result)
            [[1, 6], [8, 10], [15, 18]]

            >>> nums = [[1, 2],[3, 4],[5, 6],[7, 8]]
            >>> intervals = create(nums)
            >>> result = s.merge(intervals)
            >>> s.show(result)
            [[1, 2], [3, 4], [5, 6], [7, 8]]

            >>> nums = [[1, 2], [2, 3], [3, 4], [5, 6],[7, 8]]
            >>> intervals = create(nums)
            >>> result = s.merge(intervals)
            >>> s.show(result)
            [[1, 4], [5, 6], [7, 8]]

            >>> nums = [[1, 4], [0, 4]]
            >>> intervals = create(nums)
            >>> result = s.merge(intervals)
            >>> s.show(result)
            [[0, 4]]

            >>> nums = []
            >>> intervals = create(nums)
            >>> result = s.merge(intervals)
            >>> s.show(result)
            []

            >>> nums = [[1, 2]]
            >>> intervals = create(nums)
            >>> result = s.merge(intervals)
            >>> s.show(result)
            [[1, 2]]

            >>> nums = [[1, 4],[2, 3]]
            >>> intervals = create(nums)
            >>> result = s.merge(intervals)
            >>> s.show(result)
            [[1, 4]]

            >>> nums = [[1, 4], [2, 3], [5,9 ], [7, 8]]
            >>> intervals = create(nums)
            >>> result = s.merge(intervals)
            >>> s.show(result)
            [[1, 4], [5, 9]]

            >>> nums = [[1, 4], [4, 5]]
            >>> intervals = create(nums)
            >>> result = s.merge(intervals)
            >>> s.show(result)
            [[1, 5]]

            >>> nums = [[1, 4], [0, 2], [3, 5]]
            >>> intervals = create(nums)
            >>> result = s.merge(intervals)
            >>> s.show(result)
            [[0, 5]]

            >>> nums = [[1, 4], [0, 4]]
            >>> intervals = create(nums)
            >>> result = s.merge(intervals)
            >>> s.show(result)
            [[0, 4]]

            >>> nums = [[1, 4], [0, 0]]
            >>> intervals = create(nums)
            >>> result = s.merge(intervals)
            >>> s.show(result)
            [[0, 0], [1, 4]]

            >>> nums = [[1, 3], [2, 2], [3, 4]]
            >>> intervals = create(nums)
            >>> result = s.merge(intervals)
            >>> s.show(result)
            [[1, 4]]

            >>> nums = [[2, 3], [4, 5], [6, 7], [8, 9],[1, 10]]
            >>> intervals = create(nums)
            >>> result = s.merge(intervals)
            >>> s.show(result)
            [[1, 10]]
        """
        length = len(intervals)
        intervals.sort(key=lambda x: x.start)  # 按照每一个区间的左值进行升序排序
        if length < 2:
            return intervals
        result = []
        pre, nxt = intervals[0], intervals[1]
        cursor = 1
        while cursor < length:
            if pre.end < nxt.start:
                # b1 < a2, meanwhile a1 <= b2
                result.append(pre)
                pre = nxt
            else:
                # b1 >= a2
                if pre.end >= nxt.end:
                    # b1 >= b2
                    end = pre.end
                else:
                    # b1 < b2
                    end = nxt.end
                pre = Interval(pre.start, end)
            cursor += 1
            if cursor == length:
                result.append(pre)
                break
            nxt = intervals[cursor]
        return result

    def show(self, array):
        result = []
        for val in array:
            result.append([val.start, val.end])
        return result


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
