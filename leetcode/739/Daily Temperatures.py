"""Daily Temperatures

"""
import doctest


class Solution:
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        count = 0
        today, next_day = 0, 1
        wait_days = []
        while today < len(T) - 1:
            if T[next_day] > T[today]:
                wait_days.append(next_day - today)
                today += 1
                next_day = today + 1
            else:
                next_day += 1
                if next_day == len(T):
                    wait_days.append(0)
                    today += 1
                    next_day = today + 1
        return wait_days


if __name__ == "__main__":
    doctest.testmod(verbose=True)
