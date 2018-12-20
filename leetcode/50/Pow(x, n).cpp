#include <iostream>

using std::cin;
using std::cout;
using std::endl;

class Solution
{
  public:
    double myPow(double x, int n)
    {
        return pow(x, n);
    }

    double pow(double x, long long n)
    {
        if (n < 0)
        {
            return pow(1 / x, -n) * 1.0;
        }
        else if (n == 0)
        {
            return 1.0;
        }
        else if (n == 1)
        {
            return x * 1.0;
        }
        else if (n % 2 != 0)
        {
            return x * pow(x * x, (n - 1) / 2);
        }
        else
        {
            return pow(x * x, n / 2);
        }
    }
};

int main(int args, char **argv)
{
    Solution s = Solution();
    double x = 2.00000;
    int n = -2147483648;
    double result = s.myPow(x, n);
    cout << result << endl;
    x = 2.00000;
    n = 10;
    result = s.myPow(x, n);
    cout << result << endl;
    x = 2.1;
    n = 10;
    result = s.myPow(x, n);
    cout << result << endl;
    x = 2.00000;
    n = -2;
    result = s.myPow(x, n);
    cout << result << endl;
    return 0;
}