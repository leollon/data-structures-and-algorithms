"""4-sum
Develop an algorithm for the 4-sum problem.
"""


class FourSumSolution:
    def four_sum(self, array, target):
        if not array:
            return []
        array.sort()
        length = len(array)
        result = []
        left = 0
        while left < length - 3:
            mid1 = left + 1
            while mid1 < length - 2:
                mid2 = mid1 + 1
                right = length - 1
                while mid2 < right:
                    if (array[left] + array[mid1] + array[mid2] + array[right]) > target:
                        right -= 1
                    elif (array[left] + array[mid1] + array[mid2] + array[right]) < target:
                        mid2 += 1
                    else:
                        result.append(
                            (array[left], array[mid1], array[mid2], array[right]))
                        mid2 += 1
                        right -= 1
                mid1 += 1
            left += 1
        return list(set(result))
