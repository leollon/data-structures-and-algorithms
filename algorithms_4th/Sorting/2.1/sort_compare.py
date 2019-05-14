""""Sort Compare
"""
import sys
import time
import random


from selection_sort import SelectionSort
from insertion_sort import InsertionSort
from shell_sort import ShellSort


class SortCompare:
    def time_for_counting(self, alg, array):
        start = time.perf_counter()
        if alg == 'selection':
            SelectionSort().selection_sort(array)
        if alg == 'insertion':
            InsertionSort().insertion_sort(array)
        if alg == 'shell':
            ShellSort().shell_sort(array)
        # if alg == 'merge':
        #     MergeSort().merge_sort(array)
        # if alg == 'quick':
        #     QuickSort().quick_sort(array)
        # if alg == 'heap':
        #     HeapSort().heap_sort(array)
        return time.perf_counter() - start

    def random_input(self, alg, n, t):
        total = 0.0
        array = [0 for _ in range(n)]
        for _ in range(t):
            for i in range(n):
                array[i] = random.random()
            total += self.time_for_counting(alg, array)
        return total


def main():
    alg1 = sys.argv[1]
    alg2 = sys.argv[2]
    n = int(sys.argv[3])
    t = int(sys.argv[4])
    t1 = SortCompare().random_input(alg1, n, t)
    t2 = SortCompare().random_input(alg2, n, t)
    print("For %d random Doubles\n %s is" % (n, alg1), end=' ')
    print("%.1f times faster than %s\n" % (t2/t1, alg2))


if __name__ == "__main__":
    main()
