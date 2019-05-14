"""Shell Sort

"""


class ShellSort:
    def shell_sort(self, array):
        """Ascending sort

        :type array: List[int]

        Example

        >>> import random
        >>> sort = ShellSort()
        >>> nums = [random.randint(1, 1000) for _ in range(random.randint(1, 100))]
        >>> orig = nums[:]
        >>> sort.shell_sort(nums)
        >>> sorted(orig) == nums
        True

        """
        length = len(array)
        gap = 1
        while gap < length // 3:
            # 最大长度的h有序数组
            gap = gap * 3 + 1  # 1, 4, 13, 40, 121, 364, 1093, ...
        while gap > 0:
            # 将数组变为h有序
            for i in range(gap, length):
                # 将a[i]插入到a[i - h], a[i - 2 * h], a[i - 3 * h]...之中
                j = i
                while j >= gap and array[j] < array[j - gap]:
                    array[j], array[j - gap] = array[j - gap], array[j]
                    j -= gap
            gap = gap // 3  # 缩小gap，将增大子数组个数


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
