"""Top K Frequent Elements
"""


class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]

        Examples

            >>> s = Solution()
            >>> nums, k = [1, 1, 1, 2, 2, 3], 2
            >>> s.topKFrequent(nums, k)
            [1, 2]

            >>> nums, k = [3, 0, 1, 0], 1
            >>> s.topKFrequent(nums, k)
            [0]
        """
        if len(set(nums)) == 1: return [nums[0]]
        nums.sort()
        element_map = {}
        result = []
        for val in nums:
            if val not in element_map:
                element_map[val] = 1
            else:
                element_map[val] += 1
        counts = sorted(element_map.values(), reverse=True)[:k]
        for key in element_map:
            if element_map.get(key) in counts:
                result.append(key)
        return result


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
