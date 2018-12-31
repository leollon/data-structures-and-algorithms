#include <iostream>
#include <algorithm>
#include <set>

using std::cin;
using std::cout;
using std::endl;
using std::find;
using std::max;
using std::set;
using std::sort;
using std::vector;

class Solution
{
  public:
    int arrayNesting(vector<int> &nums)
    {
        if (!nums.size())
        {
            return 0;
        }
        set<int> visited_index;
        vector<int> max_length_array;
        int max_length = 1, count = 1, index = 0;
        int start = nums[index], next_ele = nums[start];
        while (1)
        {
            visited_index.insert(start);
            set<int>::iterator end = visited_index.end();
            if (next_ele != start && visited_index.find(next_ele) == end)
            {
                visited_index.insert(next_ele);
                next_ele = nums[next_ele];
                ++count;
                continue;
            }
            end = visited_index.end();
            max_length = max_length > count ? max_length : count;
            count = 1;
            index += 1;
            if (visited_index.find(index) != end)
            {
                index += 1;
            }
            if (index == nums.size())
            {
                break;
            }
            start = nums[index];
            next_ele = nums[start];
        }
        return max_length;
    }
};

int main(int argc, char **argv)
{
    vector<int> array = {8, 0, 1, 3, 2, 4, 5, 7, 1};
    Solution s = Solution();
    cout << s.arrayNesting(array) << endl;
    return 0;
}