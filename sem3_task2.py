#Необходимо написать функцию, которая
#проверяет, является ли данное бинарное
#дерево полным.

from queue import Queue

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def isCompleteTree(root):
    if root is None:
        return True
    q = Queue()
    q.put(root)
    seenNull = False
    while not q.empty():
        node = q.get()
        if node is None:
            seenNull = True
        else:
            if (seenNull):
                return False
            q.put(node.left)
            q.put(node.right)
    return True

import unittest

class TestIsCompleteTree(unittest.TestCase):

    def test1(self):
        self.assertTrue(isCompleteTree(None))

    def test2(self):
        root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
        self.assertTrue(isCompleteTree(root))

    def test3(self):
        root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, None, TreeNode(6)))
        self.assertFalse(isCompleteTree(root))

    def test4(self):
        root = TreeNode(1, TreeNode(2), TreeNode(3, None, TreeNode(7)))
        self.assertFalse(isCompleteTree(root))

    def test5(self):
        root = TreeNode(1)
        self.assertTrue(isCompleteTree(root))

    def test6(self):
        root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(2)))
        self.assertTrue(isCompleteTree(root))

    def test7(self):
        root = TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(8), TreeNode(9)), None), TreeNode(3, TreeNode(6), TreeNode(7)))
        self.assertFalse(isCompleteTree(root))
        
    def test8(self):
        root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, None, TreeNode(6)))
        self.assertFalse(isCompleteTree(root))

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
