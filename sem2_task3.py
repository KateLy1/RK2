#На вход функции подается бинарное
#дерево. Необходимо найти минимальную
#глубину дерева.

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

def minDepth(root):
    if root == None:
        return 0
    if root.left == None and root.right == None:
        return 1
    if root.left != None and root.right != None:
        return 1 + min(minDepth(root.left), minDepth(root.right))
    if root.left != None:
        return 1 + minDepth(root.left)
    if root.right != None:
        return 1 + minDepth(root.right)

import unittest

class TestMinDepth(unittest.TestCase):

    def test1(self):
        self.assertEqual(minDepth(None), 0)

    def test2(self):
        root = TreeNode(1)
        self.assertEqual(minDepth(root), 1)

    def test3(self):
        root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(6), TreeNode(7)))
        self.assertEqual(minDepth(root), 2)

    def test4(self):
        root = buildTree([1, 2, None, 3, None, None, None], 0)
        self.assertEqual(minDepth(root), 3)

    def test5(self):
        root = buildTree([1, None, 2, None, None, None, 3], 0)
        self.assertEqual(minDepth(root), 3)
        

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
