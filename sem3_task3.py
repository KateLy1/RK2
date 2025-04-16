#Реализуйте функцию, которая объединяет K
#отсортированных массивов в один
#отсортированный массив. Используйте минкучу для хранения наименьших элементов
#текущих массивов, что позволит извлекать их
#по очереди, сохраняя порядок.

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
        
    def __lt__(self, other):
        return self.val < other.val
        
        
class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, node):
        self.heap.append(node)
        self._heapify_up(len(self.heap) - 1)
        
    def pop(self):
        if not self.heap:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def __len__(self):
        return len(self.heap)
    
    def isEmpty(self):
        return len(self.heap) == 0

    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        while index > 0 and self.heap[index] < self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            index = parent_index
            parent_index = (index - 1) // 2

    def _heapify_down(self, index):
        while True:
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            smallest = index

            if left_child_index < len(self.heap) and self.heap[left_child_index] < self.heap[smallest]:
                smallest = left_child_index

            if right_child_index < len(self.heap) and self.heap[right_child_index] < self.heap[smallest]:
                smallest = right_child_index

            if smallest != index:
                self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
                index = smallest
            else:
                break
            

def mergeKSortedArrays(sortedArrays):
    minHeap = MinHeap()
    for i in range(len(sortedArrays)):
        for j in range(len(sortedArrays[i])):
            minHeap.push(sortedArrays[i][j])
    mergedArray = []
    while (len(minHeap) > 0):
        mergedArray.append(minHeap.pop())
    return mergedArray


import unittest

class TestMergeKSortedArrays(unittest.TestCase):

    def test1(self):
        self.assertEqual(mergeKSortedArrays([[1, 5, 8, 10], [], [10, 21, 34]]), [1, 5, 8, 10, 10, 21, 34])

    def test2(self):
        self.assertEqual(mergeKSortedArrays([[5, 8, 10, 14], [3, 4, 6, 9, 11, 15]]), [3, 4, 5, 6, 8, 9, 10, 11, 14, 15])

    def test3(self):
        self.assertEqual(mergeKSortedArrays([[8], [1], [16]]), [1, 8, 16])

    def test4(self):
        self.assertEqual(mergeKSortedArrays([[], [], []]), [])

    def test5(self):
        self.assertEqual(mergeKSortedArrays([[1, 4, 8], [-16, -5, 9, 12]]), [-16, -5, 1, 4, 8, 9, 12])


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)


#Вариант2
def mergeKSortedArrays2(sortedArrays):
    mergedArray = []
    minHeap = MinHeap()
    for i in range(len(sortedArrays)):
        currentArray = sortedArrays[i]
        if (len(currentArray) > 0):
            minHeap.push([currentArray[0], i, 0])
    while not minHeap.isEmpty():
        value, arrayIdx, elementIdx = minHeap.pop()
        mergedArray.append(value)
        if (elementIdx + 1 < len(sortedArrays[arrayIdx])):
            nextElement = sortedArrays[arrayIdx][elementIdx + 1]
            minHeap.push([nextElement, arrayIdx, elementIdx + 1])
    return mergedArray

import unittest

class TestMergeKSortedArrays2(unittest.TestCase):

    def test1(self):
        self.assertEqual(mergeKSortedArrays2([[1, 5, 8, 10], [], [10, 21, 34]]), [1, 5, 8, 10, 10, 21, 34])

    def test2(self):
        self.assertEqual(mergeKSortedArrays2([[5, 8, 10, 14], [3, 4, 6, 9, 11, 15]]), [3, 4, 5, 6, 8, 9, 10, 11, 14, 15])

    def test3(self):
        self.assertEqual(mergeKSortedArrays2([[8], [1], [16]]), [1, 8, 16])

    def test4(self):
        self.assertEqual(mergeKSortedArrays2([[], [], []]), [])

    def test5(self):
        self.assertEqual(mergeKSortedArrays2([[1, 4, 8], [-16, -5, 9, 12]]), [-16, -5, 1, 4, 8, 9, 12])


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
