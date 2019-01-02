#include <iostream>
#include <vector>

using std::cin;
using std::cout;
using std::endl;
using std::vector;

class Solution
{
  public:
    vector<int> countBits(int num)
    {
        vector<int> result;
        for (int i = 0; i <= num; ++i)
        {
            int number = i;
            int count = 0;
            while (number)
            {
                if (number % 2)
                {
                    ++count;
                }
                number /= 2;
            }
            result.push_back(count);
        }
        return result;
    }

    void printOut(vector<int> result)
    {
        for (vector<int>::iterator beg = result.begin(); beg != result.end(); ++beg)
        {
            cout << *beg << ' ';
        }
        cout << endl;
    }
};

int main(int argc, char **argv)
{
    int num = 2;
    int size;
    Solution s = Solution();
    vector<int> result = s.countBits(num);
    s.printOut(result);
    num = 5;
    result = s.countBits(num);
    s.printOut(result);
    num = 10;
    result = s.countBits(num);
    s.printOut(result);
    return 0;
}