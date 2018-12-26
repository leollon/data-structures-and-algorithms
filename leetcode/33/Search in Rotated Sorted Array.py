class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        
        Examples:

            >>> s = Solution()
            >>> nums, target = [0, 1, 2, 4, 6, 7, 8], 0
            >>> s.search(nums, target)
            0
            >>> nums, target = [8, 0, 1, 2, 4, 6, 7], 0
            >>> s.search(nums, target)
            1
            >>> nums, target = [6, 7, 8, 0, 1, 2, 4], 0
            >>> s.search(nums, target)
            3
            >>> nums, target = [], 0
            >>> s.search(nums, target)
            -1
            >>> nums, target = [2, 1], 1
            >>> s.search(nums, target)
            1
            >>> nums, target = [1], 1
            >>> s.search(nums, target)
            0
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2

            if nums[left] <= nums[mid]:
                # 左半区是否的是递增区间
                if nums[left] <= target < nums[mid]:
                    # 要查询的值在左半区递增区间中
                    right = mid - 1
                else:
                    # 要查找的的值不在该递增区间中
                    left = mid + 1
            else:
                # 如果左半区不是递增区间，则右半区一定是递增区间
                if nums[mid] < target <= nums[right]:
                    # 要查找的值在右半区递增区间中
                    left = mid + 1
                else:
                    # 要查找的的值不在该递增区间中
                    right = mid - 1

            if nums[mid] == target:
                return mid
        return -1


class EasySolution:
    def search(self, nums, target):

        """
        :type nums: List[int]
        :type target: int
        :rtype: int
            
        Examples:

            >>> s = EasySolution()
            >>> nums, target = [0, 1, 2, 4, 6, 7, 8], 0
            >>> s.search(nums, target)
            0
            >>> nums, target = [8, 0, 1, 2, 4, 6, 7], 0
            >>> s.search(nums, target)
            1
            >>> nums, target = [6, 7, 8, 0, 1, 2, 4], 0
            >>> s.search(nums, target)
            3
            >>> nums, target = [], 0
            >>> s.search(nums, target)
            -1
            >>> nums, target = [2, 1], 1
            >>> s.search(nums, target)
            1
            >>> nums, target = [1], 1
            >>> s.search(nums, target)
            0
        """
        if target in nums:
            return nums.index(target)
        return -1


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
