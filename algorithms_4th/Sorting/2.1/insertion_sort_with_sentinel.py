"""Insertion Sort with sentinel

Find the minimum value and then swap to leftmost, which can leave out `j > 0`.

Note that this can avoid corner case to be checked, and that value is so called
sentinel.
"""


class InsertionSort:
    def insertion_sort(self, array):
        """Insertion sort
        :type array: List[int]

        Example

        >>> sort = InsertionSort()
        >>> import random
        >>> nums = [random.randint(1, 10) for i in range(random.randint(1, 20))]
        >>> orig = nums[:]
        >>> sort.insertion_sort(nums)
        >>> sorted(orig) == nums
        True
        >>> nums = [random.randint(10, 999) for i in range(random.randint(1, 20))]
        >>> orig = nums[:]
        >>> sort.insertion_sort(nums)
        >>> sorted(orig) == nums
        True
        >>> nums = [3, 2, 1, 2, 1, 3]
        >>> orig = nums[:]
        >>> sort.insertion_sort(nums)
        >>> sorted(orig) == nums
        True
        """
        for i in range(1, len(array)):
            # 这里从1开始而不是从0开始，是因为需要两张牌才可进行大小比较
            j = i
            min_index = i - 1
            while j < len(array):
                if array[j] < array[min_index]:
                    min_index = j
                j += 1
            array[i - 1], array[min_index] = array[min_index], array[i - 1]


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
