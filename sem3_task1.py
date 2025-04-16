#Напишите функцию, которая проверяет, является
#ли заданный массив корректной кучей (минимум
#или максимум). Алгоритм должен проверить, что
#все узлы удовлетворяют свойству кучи.


def isMaxHeap(arr):
    n = len(arr)
    for i in range((n - 2) // 2 + 1):
        left = 2 * i + 1
        right = 2 * i + 2
        if (left < n and arr[i] < arr[left]):
            return False
        if (right < n and arr[i] < arr[right]):
            return False
    return True

import unittest

class TestIsMaxHeap(unittest.TestCase):

    def test1(self):
        self.assertTrue(isMaxHeap([]))

    def test2(self):
        self.assertTrue(isMaxHeap([5]))

    def test3(self):
        self.assertTrue(isMaxHeap([9, 4, 7, 1, -2, 6, 5]))

    def test4(self):
        self.assertFalse(isMaxHeap([1, 2, 3, 4, 5]))

    def test5(self):
        self.assertFalse(isMaxHeap([5, 3, 8]))


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)



#Обход макскучи в ширину
from queue import Queue

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
        
def buildTree(arr, i):
    if i >= len(arr):
        return None
    root = TreeNode(arr[i])
    root.left = buildTree(arr, 2 * i + 1)
    root.right = buildTree(arr, 2 * i + 2)
    return root

def isMaxHeap2(root):
    if not root:
        return True
    q = Queue() 
    q.put(root)
    shouldBeLeaf = False
    while not q.empty():
        current = q.get()
        if (current.left):
            if (shouldBeLeaf or current.left.val > current.val):
                return False
            q.put(current.left)
        else:
            shouldBeLeaf = True
        if (current.right):
            if (shouldBeLeaf or current.right.val > current.val):
                return False
            q.put(current.right)
        else:
            shouldBeLeaf = True
    return True

import unittest

class TestIsMaxHeap2(unittest.TestCase):

    def test1(self):
        root = None
        self.assertTrue(isMaxHeap2(root))

    def test2(self):
        root = TreeNode(1)
        self.assertTrue(isMaxHeap2(root))

    def test3(self):
        root = buildTree([9, 4, 7, 1, -2, 6, 5], 0)
        self.assertTrue(isMaxHeap2(root))

    def test4(self):
        root = buildTree([1, 2, 3, 4, 5], 0)
        self.assertFalse(isMaxHeap2(root))

    def test5(self):
        root = buildTree([5, 3, 8], 0)
        self.assertFalse(isMaxHeap2(root))


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
