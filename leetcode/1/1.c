/*
 * Given an array of integers, return indices of the two numbers such that they
 * add up to a specific target.
 * 
 * You may assume that each input would have exactly one solution, and you may
 * not use the same element twice.
 * 
 * Example:
 * Given nums = [2, 7, 11, 15], target = 9,
 * Because nums[0] + nums[1] = 2 + 7 = 9,
 * return [0, 1].
*/

#include <stdio.h>
#include <stdlib.h>

int *twoSum(int *nums, int numsSize, int target);

int main()
{
    int nums[] = {2, 7, 11, 16};
    int target = 9;
    int *ret_arr = twoSum(nums, 4, target);
    printf("%d %d\n", ret_arr[0], ret_arr[1]);
    nums[0] = 3;
    nums[1] = 2;
    nums[2] = 4;
    target = 6;
    ret_arr = twoSum(nums, 3, target);
    printf("%d %d\n", ret_arr[0], ret_arr[1]);
    return 0;
}

int *twoSum(int *nums, int numsSize, int target)
{
    int *arr = (int *)malloc(sizeof(int) * 2);
    int i = 0, j = numsSize;
    while (1)
    {
        if (nums[i] + nums[j] == target)
        {
            arr[0] = i;
            arr[1] = j;
            break; // 找到即退出循环
        }
        j -= 1;
        if (j == i)
        {
            // 右边游标到达左端
            ++i;
            j = numsSize - 1;
            if (i == numsSize - 1)
            {
                // 左边游标到达最右端
                break;
            }
        }
    }
    return arr;
}