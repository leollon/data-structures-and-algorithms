"""Summary Ranges
Given a sorted integer array without duplicates, return the summary of its
ranges.

Example 1:

    Input:  [0,1,2,4,5,7]
    Output: ["0->2","4->5","7"]
    Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.

Example 2:

    Input:  [0,2,3,4,6,8,9]
    Output: ["0","2->4","6","8->9"]
    Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.
"""


class Solution:
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]

        Examples

            >>> s = Solution()
            >>> nums = [0, 1, 2, 4, 5, 7]
            >>> s.summaryRanges(nums)
            ['0->2', '4->5', '7']

            >>> nums = [0, 2, 3, 4, 6, 8, 9]
            >>> s.summaryRanges(nums)
            ['0', '2->4', '6', '8->9']

            >>> nums = [0, 1, 2, 3, 4, 5, 6]
            >>> s.summaryRanges(nums)
            ['0->6']

            >>> nums = [0, 1, 2, 3, 3, 4, 5, 5, 7, 7, 9, 10]
            >>> s.summaryRanges(nums)
            ['0->5', '7', '9->10']

            >>> nums = [0, 2, 3, 4, 6, 7, 9, 11]
            >>> s.summaryRanges(nums)
            ['0', '2->4', '6->7', '9', '11']

            >>> nums = [0, 2, 4, 6, 8, 10]
            >>> s.summaryRanges(nums)
            ['0', '2', '4', '6', '8', '10']

            >>> nums = [0, 2, 4, 7, 8, 10]
            >>> s.summaryRanges(nums)
            ['0', '2', '4', '7->8', '10']

            >>> nums = [0, 1]
            >>> s.summaryRanges(nums)
            ['0->1']

            >>> nums = [0]
            >>> s.summaryRanges(nums)
            ['0']

            >>> nums = [0, 2]
            >>> s.summaryRanges(nums)
            ['0', '2']

        """
        results = []
        if not nums:
            return results
        left, right = 0, 1
        while right < len(nums):
            if nums[right] - nums[right - 1] >= 2:
                if nums[right - 1] == nums[left]:
                    results.append(str(nums[left]))
                else:
                    results.append("%d->%d" % (nums[left], nums[right - 1]))
                left = right
            right += 1
        if left == len(nums) - 1:
            results.append(str(nums[left]))
        else:
            if nums[left] == nums[right - 1]:
                results.append(str(nums[left]))
            else:
                results.append("%d->%d" % (nums[left],  nums[right - 1]))
        return results


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
