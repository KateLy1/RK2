#Дано бинарное дерево. Необходимо подсчитать количество
#зеркальных узлов в нем

def buildTree(arr, i):
    if i >= len(arr):
        return None
    root = TreeNode(arr[i])
    root.left = buildTree(arr, 2 * i + 1)
    root.right = buildTree(arr, 2 * i + 2)
    return root

def dfs(left, right):
    if left == None or right == None:
        return 0
    count = 0
    if left.data == right.data:
        count = 1
    count += dfs(left.left, right.right)
    count += dfs(left.right , right.left)
    return count

def CountMirrorTwins(root):
    if root == None:
        return 0
    return dfs(root.left, root.right)

import unittest

class TestCountMirrorTwins(unittest.TestCase):

    def test1(self):
        self.assertEqual(CountMirrorTwins(None), 0)

    def test2(self):
        root = TreeNode(1)
        self.assertEqual(CountMirrorTwins(root), 0)

    def test3(self):
        root = buildTree([1, 2, 2], 0)
        self.assertEqual(CountMirrorTwins(root), 1)

    def test4(self):
        root = buildTree([1, 2, 2, 3, 4, 4, 3], 0)
        self.assertEqual(CountMirrorTwins(root), 3)

    def test5(self):
        root = buildTree([1, 2, 3, 4, 5, 6, 7], 0)
        self.assertEqual(CountMirrorTwins(root), 0)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
