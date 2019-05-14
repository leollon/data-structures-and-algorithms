"""Insertion Sort

Complexity:

    average:
        ~N*N/4 compares and ~N*N/4 exchanges, array is almost in order.
    worst:
        ~N*N/2 compares and ~N*N/2 exchanges, array is in reversed order.
    best:
        N - 1 compares and 0 exchanges，array is already in order.
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
        """
        for i in range(1, len(array)):
            # 这里从1开始而不是从0开始，是因为需要两张牌才可进行大小比较
            j = i
            while j > 0 and array[j] < array[j - 1]:
                # 左侧牌相邻进行大小比较，并进行交换
                array[j], array[j - 1] = array[j - 1], array[j]
                j -= 1


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
