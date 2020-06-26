"""

"""
import unittest
from typing import List


class Solution:
    def simplifyPath(self, path: str) -> str:

        directories = []
        for directory in path.split("/"):
            if directory:
                if directory != "." and directory != "..":
                    directories.append(directory)
                if directory == ".." and directories:
                    directories.pop()
        return "/" + "/".join(directories)


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_simplifyPath(self):

        s = "/home/"
        self.assertEqual("/home", self.solution.simplifyPath(s))

        s = "/-////ifej/ajeoe/-><<///../../"
        self.assertEqual("/-/ifej", self.solution.simplifyPath(s))

        s = "/../"
        self.assertEqual("/", self.solution.simplifyPath(s))

        s = "/home//foo"
        self.assertEqual("/home/foo", self.solution.simplifyPath(s))

        s = "/home////ba.b/"
        self.assertEqual("/home/ba.b", self.solution.simplifyPath(s))

        s = "/home////ba.b/../"
        self.assertEqual("/home", self.solution.simplifyPath(s))

        s = "/a/./b///../../c/"
        self.assertEqual("/c", self.solution.simplifyPath(s))

        s = "/a/./b///../../c/.."
        self.assertEqual("/", self.solution.simplifyPath(s))


if __name__ == "__main__":
    unittest.main()

