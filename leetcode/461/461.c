/*
 * The Hamming distance between two integers is the number of positions
 * at which the corresponding bits are different.
 * 
 * Given two integers x and y, calculate the Hamming distance.
 * 
 * Note:
 * 0 ≤ x, y < 231.
 * 
 * Example:
 * Input: x = 1, y = 4
 * 
 * Output: 2
 * 
 * Explanation:
 * 
 * 1   (0 0 0 1)
 * 4   (0 1 0 0)
 *        ↑   ↑
 * 
 * The above arrows point to positions where the corresponding bits are
 * different.
 * 
*/

#include <stdio.h>

int hammingDistance(int x, int y)
{
    int max, count = 0;
    max = x > y ? x : y;
    while (max)
    {
        if ((x % 2) ^ (y % 2) == 1)
        {
            count += 1;
        }
        max /= 2;
        x /= 2;
        y /= 2;
    }
    return count;
}

int main()
{
    int x = 1, y = 4;
    printf("%d", hammingDistance(x, y));
    x = 1, y = 5;
    printf("%d", hammingDistance(x, y));
    x = 2, y = 5;
    printf("%d", hammingDistance(x, y));
    return 0;
}