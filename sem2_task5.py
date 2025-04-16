#На вход функции подается 2 бинарных
#дерева.
#Необходимо понять, являются ли эти
#два дерева одинаковыми.

def isSameTree(a, b):
    if a == None and b == None:
        return True
    if a == None or b == None:
        return False
    if a.data != b.data:
        return False
    return isSameTree(a.left, b.left) and isSameTree(a.right, b.right)

import unittest

class TestIsSameTree(unittest.TestCase):

    def test1(self):
        self.assertTrue(isSameTree(None, None))

    def test2(self):
        root1 = TreeNode(1)
        root2 = TreeNode(1)
        self.assertTrue(isSameTree(root1, root2))

    def test3(self):
        root1 = buildTree([1, 2, 2, 3, 4, 4, 3], 0)
        root2 = buildTree([1, 2, 5, 3, 4, 4, 3], 0)
        self.assertFalse(isSameTree(root1, root2))

    def test4(self):
        root1 = buildTree([1, 2, 2, None, 3, None, 3], 0)
        root2 = buildTree([1, 2, 2, None, 3, None, 3], 0)
        self.assertTrue(isSameTree(root1, root2))

    def test5(self):
        root2 = buildTree([1, 2, 2, 3, 4, 4, 5], 0)
        self.assertFalse(isSameTree(None, root2))

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)


#На вход функции подается два бинарных дерева. Необходимо
#вернуть true, если дерево B является поддеревом для A

def isSubtree(A, B):
    if (B == None):
        return True
    if (A == None):
        return False
    if (isSameTree(A, B)):
        return True
    return isSubtree(A.left, B) or isSubtree(A.right, B)

import unittest

class TestIsSubtree(unittest.TestCase):

    def test1(self):
        root1 = buildTree([1, 2, 2, 3, 4, 4, 3], 0)
        self.assertTrue(isSubtree(root1, None))

    def test2(self):
        root2 = buildTree([1, 2, 2, 3, 4, 4, 3], 0)
        self.assertFalse(isSubtree(None, root2))

    def test3(self):
        root1 = buildTree([1, 2, 2, 3, 4, 4, 3], 0)
        root2 = buildTree([1, 2, 2, 3, 4, 4, 3], 0)
        self.assertTrue(isSubtree(root1, root2))

    def test4(self):
        root1 = buildTree([3, 4, 5, 1, 2], 0)
        root2 = buildTree([4, 1, 2], 0)
        self.assertTrue(isSubtree(root1, root2))

    def test5(self):
        root1 = buildTree([1, 2, 3], 0)
        root2 = buildTree([3, 4, 5], 0)
        self.assertFalse(isSubtree(root1, root2))

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
