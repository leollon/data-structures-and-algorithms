"""Time Based Key-Value Store
Create a timebased key-value store class TimeMap, that supports two operations.

1. set(string key, string value, int timestamp)

Stores the key and value, along with the given timestamp.
2. get(string key, int timestamp)

Returns a value such that set(key, value, timestamp_prev) was called previously,
with timestamp_prev <= timestamp.
If there are multiple such values, it returns the one with the largest timestamp_prev.
If there are no values, it returns the empty string ("").
 

Example 1:

Input: inputs = ["TimeMap","set","get","get","set","get","get"], inputs = [[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]]
Output: [null,null,"bar","bar",null,"bar2","bar2"]
Explanation:   
TimeMap kv;   
kv.set("foo", "bar", 1); // store the key "foo" and value "bar" along with timestamp = 1   
kv.get("foo", 1);  // output "bar"   
kv.get("foo", 3); // output "bar" since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 ie "bar"   
kv.set("foo", "bar2", 4);   
kv.get("foo", 4); // output "bar2"   
kv.get("foo", 5); //output "bar2"   

Example 2:

Input: inputs = ["TimeMap","set","set","get","get","get","get","get"], inputs = [[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]
Output: [null,null,null,"","high","high","low","low"]
 

Note:

    1. All key/value strings are lowercase.
    2. All key/value strings have length in the range [1, 100]
    3. The timestamps for all TimeMap.set operations are strictly increasing.
    4. 1 <= timestamp <= 10^7
    TimeMap.set and TimeMap.get functions will be called a total of 120000
times (combined) per test case.
"""
import collections  # built-in data structure
import bisect  # binary search
import unittest


class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._table = collections.defaultdict(list)
        

    def set(self, key: 'str', value: 'str', timestamp: 'int') -> 'None':
        self._table[key].append((timestamp, value))

    def get(self, key: 'str', timestamp: 'int') -> 'str':
        values = self._table.get(key, None)
        if not values: return ""
        # find the first one to larger than timestamp, return its index,
        # otherwise return 0
        cursor = bisect.bisect(values, (timestamp, chr(127)))
        if not cursor: return ""
        return self._table[key][cursor - 1][1]


class TestTimeMap(unittest.TestCase):

    @staticmethod
    def create_time_map():
        return TimeMap()

    def test_get(self):
        time_map = self.create_time_map()
        time_map.set("foo", "bar", 1)
        self.assertEqual("bar", time_map.get("foo", 1))
        self.assertEqual("bar", time_map.get("foo", 2))
        self.assertEqual("bar", time_map.get("foo", 3))

        time_map.set("foo", "bar2", 4)
        self.assertEqual("bar2", time_map.get("foo", 4))
        self.assertEqual("bar2", time_map.get("foo", 5))

        time_map.set("foo", "bar6", 6)
        self.assertEqual("bar", time_map.get("foo", 1))
        self.assertEqual("bar", time_map.get("foo", 2))
        self.assertEqual("bar4", time_map.get("foo", 4))


if __name__ == "__main__":
    unittest.main()
