#Восстановление бинароного дерева из массива
class TreeNode:
    def __init__(self, data = 0, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

def buildTree(arr, i):
    if i >= len(arr):
        return None
    root = TreeNode(arr[i])
    root.left = buildTree(arr, 2 * i + 1)
    root.right = buildTree(arr, 2 * i + 2)
    return root

def tree_to_list(root):
    if root is None:
        return []
    queue = [root]
    result = []
    while queue:
        node = queue.pop(0)
        if node is not None:
            result.append(node.data)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    return result

import unittest

class TestBuildTree(unittest.TestCase):

    def test1(self):
        root = buildTree([], 0)
        self.assertIsNone(root)

    def test2(self):
        root = buildTree([1], 0)
        self.assertEqual(root.data, 1)
        self.assertIsNone(root.left)
        self.assertIsNone(root.right)

    def test3(self):
        arr = [1, 2, 3, 4, 5, 6, 7]
        root = buildTree(arr, 0)
        expected_list = [1, 2, 3, 4, 5, 6, 7]
        actual_list = tree_to_list(root)
        self.assertEqual(actual_list, expected_list)

    def test4(self):
        arr = [1, 2, 3, 4, 5, None, 7]
        root = buildTree(arr, 0)
        expected_list = [1, 2, 3, 4, 5, None, 7]
        actual_list = tree_to_list(root)
        self.assertEqual(actual_list, expected_list)

    def test5(self):
        arr = [1, 2, None, 4, 5, None, None]
        root = buildTree(arr, 0)
        expected_list = [1, 2, None, 4, 5]
        actual_list = tree_to_list(root)
        self.assertEqual(actual_list, expected_list)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
