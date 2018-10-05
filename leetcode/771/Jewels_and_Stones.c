/*
 * You're given strings J representing the types of stones that are jewels,
 * and S representing the stones you have.Each character in S is a type of
 * stone you have.You want to know how many of the stones you have are also
 * jewels.
 * 
 * The letters in J are guaranteed distinct,
 * and all characters in J and S are
 * letters.Letters are case sensitive,
 * so "a" is considered a different type of
 * stone from "A".
 * 
 * Example 1 :
 * 
 * Input : J = "aA", S = "aAAbbbb"
 * Output : 3
 * 
 * Example 2 :
 * Input : J = "z", S = "ZZ"
 * Output : 0
 * 
 *  Note :
 *  S and J will consist of letters and have length at most 50.
 *  The characters in J are distinct.
 */

#include <stdio.h>

int numJewelsInStones(char *J, char *S)
{
    int count = 0;
    int i = 0, j = 0;
    while (J[i] != '\0')
    {
        while (S[j] != '\0')
        {
            if (J[i] == S[j])
            {
                ++count;
            }
            ++j;
        }
        ++i;
        j = 0;
    }
    return count;
}
int main()
{
    char J[] = "aA",
         S[] = "aAAbbbbb";
    printf("%d", numJewelsInStones(J, S));
    return 0;
}