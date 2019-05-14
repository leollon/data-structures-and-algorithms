"""Selection Sort

Use ~N*N/2 compres and N exchanges to sort an array of length N.
"""


class SelectionSort:
    def selection_sort(self, array):
        """
        :type array: List[int]

        Example

        >>> sort = SelectionSort()
        >>> import random
        >>> nums = [random.randint(1, 10) for i in range(random.randint(1, 100))]
        >>> orig = nums[:]
        >>> sort.selection_sort(nums)
        >>> sorted(orig) == nums
        True
        """
        for i in range(0, len(array)):
            min_value_index = i
            for j in range(i + 1, len(array)):
                if array[j] < array[min_value_index]:
                    min_value_index = j
            if min_value_index != i:
                array[min_value_index], array[i] = array[i], array[min_value_index]


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
