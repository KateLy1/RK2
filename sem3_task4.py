#К-ый наименьший элемент в BST
#Вариант 1
class TreeNode:
    def __init__ (self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
        
def buildTree(arr, i):
    if (i >= len(arr)):
        return None
    root = TreeNode(arr[i])
    root.left = buildTree(arr, 2 * i + 1)
    root.right = buildTree(arr, 2 * i + 2)
    return root

def inorderMinIterative(node, k):
    stack = []
    counter = 0
    current = node
    while (len(stack) > 0 or current != None):
        while (current != None):
            stack.append(current)
            current = current.left
        current = stack.pop()
        counter += 1
        if (counter == k):
            return current.val
        current = current.right
    return None

class TestInorderMinIterative(unittest.TestCase):

    def test1(self):
        self.assertIsNone(inorderMinIterative(None, 1))

    def test2(self):
        root = buildTree([1, 2, 3], 0)
        self.assertIsNone(inorderMinIterative(root, 4))

    def test3(self):
        root = buildTree([5, 3, 7, 1, 4], 0)
        self.assertEqual(inorderMinIterative(root, 1), 1)
        self.assertEqual(inorderMinIterative(root, 2), 3)
        self.assertEqual(inorderMinIterative(root, 3), 4)
        self.assertEqual(inorderMinIterative(root, 4), 5)

    def test4(self):
        root = TreeNode(3)
        root.left = TreeNode(1)
        root.right = TreeNode(4)
        root.left.right = TreeNode(2)
        self.assertEqual(inorderMinIterative(root, 2), 2)

    def test5(self):
        root = buildTree([5], 0)
        self.assertEqual(inorderMinIterative(root, 1), 5)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)


#Вариант 2
#К-ый наименьший элемент в BST

class TreeNode:
    def __init__ (self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
        
def buildTree(arr, i):
    if (i >= len(arr)):
        return None
    root = TreeNode(arr[i])
    root.left = buildTree(arr, 2 * i + 1)
    root.right = buildTree(arr, 2 * i + 2)
    return root

def inorderMin(node, k, counter):
    if (node == None):
        return None
    leftResult = inorderMin(node.left, k, counter)
    if (leftResult != None):
        return leftResult
    counter[0] += 1
    if (counter[0] == k):
        return node.val
    return inorderMin(node.right, k, counter)

import unittest

class TestInorderMin(unittest.TestCase):

    def test1(self):
        self.assertIsNone(inorderMin(None, 1, 0))

    def test2(self):
        root = buildTree([2, 1, 3], 0)
        self.assertEqual(inorderMin(root, 2, [0]), 2)

    def test3(self):
        root = buildTree([5, 3, 7, 2, 4, 6, 8], 0)
        self.assertEqual(inorderMin(root, 3, [0]), 4)

    def test4(self):
        root = buildTree([5, 3, 7], 0)
        self.assertEqual(inorderMin(root, 1, [0]), 3)

    def test5(self):
        root = buildTree([5], 0)
        self.assertEqual(inorderMin(root, 1, [0]), 5)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
