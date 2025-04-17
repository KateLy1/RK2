#Симметричное ли бинарное дерево (в ширину)

#Вариант BFS
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

def isSymmetric(root):
    if root == None:
        return True
    queue = [root]
    while (len(queue) > 0):
        queueLen = len(queue)
        for i in range(queueLen):
            if (queue[i] == None and queue[queueLen - i - 1] == None):
                continue
            if (queue[i] == None or queue[queueLen - i - 1] == None):
                return False
            if (queue[i].data != queue[queueLen - i - 1].data):
                return False
            queue.append(queue[i].left)
            queue.append(queue[i].right)
        queue = queue[queueLen:]
    return True

import unittest

class TestIsSymmetric(unittest.TestCase):

    def test1(self):
        self.assertTrue(isSymmetric(None))

    def test2(self):
        root = TreeNode(1)
        self.assertTrue(isSymmetric(root))

    def test3(self):
        root = buildTree([1, 2, 2, 3, 4, 4, 3], 0)
        self.assertTrue(isSymmetric(root))

    def test4(self):
        root = buildTree([1, 2, 2, None, 3, None, 3], 0)
        self.assertFalse(isSymmetric(root))

    def test5(self):
        root = buildTree([1, 2, 2, 3, 4, 4, 5], 0)
        self.assertFalse(isSymmetric(root))

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)


#Вариант DFS
#Симметричное ли бинарное дерево (в глубину)
def deptSearch(root, res):
    if root == None:
        return res
    deptSearch(root.left, res)
    res.append(root.data)
    deptSearch(root.right, res)
    return res

def isSymmetricDFS (root):
    if root == None:
        return True
    data = []
    data = deptSearch(root, data)
    j = len(data) - 1
    for i in range (len(data)//2):
        if data[i] != data[j]:
            return False
        j -= 1
    return True

import unittest

class TestIsSymmetric(unittest.TestCase):

    def test1(self):
        self.assertTrue(isSymmetricDFS(None))

    def test2(self):
        root = TreeNode(1)
        self.assertTrue(isSymmetricDFS(root))

    def test3(self):
        root = buildTree([1, 2, 2, 3, 4, 4, 3], 0)
        self.assertTrue(isSymmetricDFS(root))

    def test4(self):
        root = buildTree([1, 2, 2, None, 3, None, 3], 0)
        self.assertFalse(isSymmetricDFS(root))

    def test5(self):
        root = buildTree([1, 2, 2, 3, 4, 4, 5], 0)
        self.assertFalse(isSymmetricDFS(root))

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
