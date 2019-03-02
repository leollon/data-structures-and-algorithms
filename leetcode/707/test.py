import unittest
from Design_Linked_List import MyLinkedList


class TestSolution(unittest.TestCase):

    def test_linkedlist(self):
        head = MyLinkedList()
        op_map = {
            "addAtHead": head.addAtHead,
            "addAtIndex": head.addAtIndex,
            "addAtTail": head.addAtTail,
            "deleteAtIndex": head.deleteAtIndex,
            "get": head.get
        }

        # 1
        operations = [
            "addAtHead", "addAtIndex", "addAtIndex", "addAtTail", "addAtHead",
            "addAtIndex", "addAtIndex", "addAtIndex", "addAtTail", "addAtTail",
            "deleteAtIndex"
        ]
        data = [[0], [1, 9], [1, 5], [7], [1], [5, 8], [5, 2], [3, 0], [1],
                [0], [6]]
        result = [
            None, None, None, None, None, None, None, None, None, None, None
        ]
        ans = []
        for index, op in enumerate(operations):
            ans.append(op_map[op](*data[index]))
        self.assertEqual(result, ans)

        # 2
        head.clear()
        ans.clear()

        operations = ["addAtHead", "addAtIndex", "get", "get", "get"]
        data = [[1], [1, 2], [1], [0], [2]]
        result = [None, None, 2, 1, -1]
        for index, op in enumerate(operations):
            ans.append(op_map[op](*data[index]))
        self.assertEqual(result, ans)

        # 3
        head.clear()
        ans.clear()

        operations = [
            "addAtHead", "addAtHead", "addAtHead", "addAtIndex",
            "deleteAtIndex", "addAtHead", "addAtTail", "get", "addAtHead",
            "addAtIndex", "addAtHead"
        ]
        data = [[7], [2], [1], [3, 0], [2], [6], [4], [4], [4], [5, 0], [6]]
        result = [
            None, None, None, None, None, None, None, 4, None, None, None
        ]
        for index, op in enumerate(operations):
            ans.append(op_map[op](*data[index]))
        self.assertEqual(result, ans)

        # 4
        head.clear()
        ans.clear()

        operations = [
            "addAtIndex", "addAtIndex", "addAtIndex", "addAtIndex",
            "addAtIndex", "addAtIndex", "get"
        ]
        data = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [1]]
        result = [None, None, None, None, None, None, 2]
        for index, op in enumerate(operations):
            ans.append(op_map[op](*data[index]))
        self.assertEqual(result, ans)

        # 5
        head.clear()
        ans.clear()

        operations = [
            "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex",
            "get"
        ]
        data = [[1], [3], [1, 2], [1], [1], [1]]
        result = [None, None, None, 2, None, 3]
        for index, op in enumerate(operations):
            ans.append(op_map[op](*data[index]))
        self.assertEqual(result, ans)

        # 6
        head.clear()
        ans.clear()
        operations = [
            "addAtHead", "addAtHead", "deleteAtIndex", "addAtIndex",
            "addAtHead", "addAtHead", "addAtHead", "get", "addAtTail",
            "addAtIndex", "addAtHead"
        ]
        result = [
            None, None, None, None, None, None, None, 2, None, None, None
        ]
        data = [[5], [2], [1], [1, 9], [4], [9], [8], [3], [1], [3, 6], [3]]
        for index, op in enumerate(operations):
            ans.append(op_map[op](*data[index]))
        self.assertEqual(result, ans)

        # 7
        head.clear()
        ans.clear()

        operations = [
            "addAtHead", "get", "addAtTail", "deleteAtIndex", "addAtHead",
            "deleteAtIndex", "get", "addAtTail", "addAtHead", "addAtTail",
            "addAtTail", "addAtTail", "addAtIndex", "get", "addAtIndex",
            "addAtHead", "deleteAtIndex", "addAtIndex", "addAtHead",
            "addAtIndex", "deleteAtIndex", "get", "addAtTail", "deleteAtIndex",
            "deleteAtIndex", "addAtTail", "addAtTail", "addAtIndex",
            "addAtHead", "get", "get", "addAtTail", "addAtTail", "addAtTail",
            "addAtTail", "addAtIndex", "addAtIndex", "addAtHead", "addAtIndex",
            "addAtTail", "addAtHead", "addAtHead", "addAtHead", "addAtHead",
            "addAtHead", "addAtHead", "addAtTail", "addAtHead",
            "deleteAtIndex", "addAtHead", "get", "addAtHead", "get",
            "addAtHead", "addAtHead", "addAtHead", "addAtIndex",
            "deleteAtIndex", "addAtTail", "deleteAtIndex", "get", "addAtIndex",
            "addAtHead", "addAtTail", "deleteAtIndex", "addAtHead",
            "addAtIndex", "deleteAtIndex", "deleteAtIndex", "deleteAtIndex",
            "addAtHead", "addAtTail", "addAtTail", "addAtHead", "addAtTail",
            "addAtIndex", "deleteAtIndex", "deleteAtIndex", "addAtIndex",
            "addAtHead", "addAtHead", "addAtTail", "get", "addAtIndex", "get",
            "addAtHead", "addAtHead", "addAtHead", "addAtIndex", "addAtIndex",
            "get", "addAtHead", "get", "get", "addAtTail", "addAtHead",
            "addAtHead", "addAtTail", "addAtTail", "get", "addAtTail"
        ]
        result = [
            None, -1, None, None, None, None, 8, None, None, None, None,
            None, None, 33, None, None, None, None, None, None, None, 14, None,
            None, None, None, None, None, None, 15, 8, None, None, None, None,
            None, None, None, None, None, None, None, None, None, None, None,
            None, None, None, None, 57, None, 69, None, None, None, None, None,
            None, None, 11, None, None, None, None, None, None, None, None,
            None, None, None, None, None, None, None, None, None, None, None,
            None, None, 0, None, 71, None, None, None, None, None, 91, None,
            77, 14, None, None, None, None, None, 14, None
        ]
        data = [[8], [1], [81], [2], [26], [2], [1], [24], [15], [0], [13],
                [1], [6, 33], [6], [2, 91], [82], [6], [4, 11], [3], [7, 14],
                [1], [6], [99], [11], [7], [5], [92], [7, 92], [57], [2], [6],
                [39], [51], [3], [22], [5, 26], [9, 52], [69], [5, 58], [79],
                [7], [41], [33], [88], [44], [8], [72], [93], [18], [1], [9],
                [46], [9], [92], [71], [69], [11, 54], [27], [83], [12], [20],
                [19, 97], [77], [36], [3], [35], [16, 68], [22], [36], [17],
                [62], [89], [61], [6], [92], [28, 69], [23], [28], [7, 4], [0],
                [24], [52], [1], [23, 3], [7], [6], [68], [79], [45, 90],
                [41, 52], [28], [25], [9], [32], [11], [90], [24], [98], [36],
                [34], [26]]
        for index, op in enumerate(operations):
            ans.append(op_map[op](*data[index]))
        self.assertEqual(result, ans)


if __name__ == "__main__":
    unittest.main()