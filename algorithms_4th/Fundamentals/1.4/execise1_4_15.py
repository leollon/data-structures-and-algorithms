"""Faster 3-sum
As a warmup, develop an implementation TwoSumFaster that
uses a linear algorithm to count the pairs that sum to zero after the array is sorted (in-
stead of the binary-search-based linearithmic algorithm). Then apply a similar idea to
develop a quadratic algorithm for the 3-sum problem.
"""


class ThreeSumFaster:
    def three_sum_faster(self, array, target):
        if not array:
            return []
        array.sort()
        result = []
        length = len(array)
        left = 0
        while left < length - 2:
            mid = left + 1
            right = length - 1
            while mid < right:
                if array[left] + array[mid] + array[right] > target:
                    right -= 1
                elif array[left] + array[mid] + array[right] < target:
                    mid += 1
                else:
                    result.append((array[left], array[mid], array[right]))
                    mid += 1
                    right -= 1
            left += 1
        return list(set(result))
