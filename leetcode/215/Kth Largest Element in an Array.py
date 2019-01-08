#!/usr/bin/python3
"""
Find the kth largest element in an unsorted array.
Note that it is the kth largest element in the sorted order,
not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note: 
You may assume k is always valid, 1 ≤ k ≤ array's length.
"""


class BestSolution:
    def findKthLargest(self, nums, k):
        """Use built-in function
        
        sort the array, makes it in descending order, then you can get the (k-1)th
        value, which is the largest element

        :type nums: List[int]
        :type k: int
        :rtype: int

        Examples

            >>> nums, k = [3, 2, 1, 5, 6, 4], 1
            >>> BestSolution().findKthLargest(nums, k)
            6
            >>> nums, k = [-3, -2, -1, -5, -6, -4, 0], 2
            >>> BestSolution().findKthLargest(nums, k)
            -1
            >>> nums, k = [-3, -2, -1, -5, -6, -4], 2
            >>> BestSolution().findKthLargest(nums, k)
            -2
            >>> nums, k = [-3, -2, -1, -5, -5, -5, -5, -5, -5, -6, -4], 7
            >>> BestSolution().findKthLargest(nums, k)
            -5
            >>> nums, k = [-3, -2, -1, -5, -5, -5, -5, -5, -4], 6
            >>> BestSolution().findKthLargest(nums, k)
            -5
            >>> nums, k = [-2, -2, -2, -2], 1
            >>> BestSolution().findKthLargest(nums, k)
            -2
            >>> nums, k = [7, 8, 9], 3
            >>> BestSolution().findKthLargest(nums, k)
            7
            >>> nums, k = [9, 8, 6], 3
            >>> BestSolution().findKthLargest(nums, k)
            6
        """
        if len(nums) == 0 or k<=0: return None
        return sorted(nums, reverse=True)[k - 1]


class HeapSolution:
    def findKthLargest(self, nums, k):
        """Use a heap

        Maintain a heap, which holds the first Kth values

        :type nums: List[int]
        :type k: int
        :rtype: int

        Examples

            >>> nums, k = [3, 2, 1, 5, 6, 4], 1
            >>> HeapSolution().findKthLargest(nums, k)
            6
            >>> nums, k = [-3, -2, -1, -5, -6, -4, 0], 2
            >>> HeapSolution().findKthLargest(nums, k)
            -1
            >>> nums, k = [-3, -2, -1, -5, -6, -4], 2
            >>> HeapSolution().findKthLargest(nums, k)
            -2
            >>> nums, k = [-3, -2, -1, -5, -5, -5, -5, -5, -5, -6, -4], 7
            >>> HeapSolution().findKthLargest(nums, k)
            -5
            >>> nums, k = [-3, -2, -1, -5, -5, -5, -5, -5, -4], 6
            >>> HeapSolution().findKthLargest(nums, k)
            -5
            >>> nums, k = [-2, -2, -2, -2], 1
            >>> HeapSolution().findKthLargest(nums, k)
            -2
            >>> nums, k = [7, 8, 9], 3
            >>> HeapSolution().findKthLargest(nums, k)
            7
            >>> nums, k = [9, 8, 6], 3
            >>> HeapSolution().findKthLargest(nums, k)
            6
            >>> nums, k = [3, 2, 3, 1, 2, 4, 5, 5, 6], 4
            >>> HeapSolution().findKthLargest(nums, k)
            4
        """
        result = []  # the heap that hold the first Kth largest values
        for val in nums:
            if len(result) == 0:
                result.append(val)
            else:
                if val >= min(result):
                    # larger than the minimum value
                    if len(result) >= k:
                        # the length of head is larger than K,
                        # so pop the first value as to add the one bigger than
                        # first value
                        result.pop(0)
                    result.append(val)
                else:
                    if len(result) < k:
                        result.append(val)
            result.sort() # make the array in ascending order
        return result[0]


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
