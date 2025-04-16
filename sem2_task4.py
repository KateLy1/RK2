#Дано бинарное дерево поиска в виде массива. Необходимо найти
#произведение минимального и максимального значений.

def maxMinMultiplication (data):
    if len(data) < 3 or None in data:
        return -1
    min_index = 1
    max_index = 2
    i = 0
    while i < len(data):
        min_index = i
        i = 2 * i + 1
    i = 0
    while i < len(data):
        max_index = i
        i = 2 * i + 2
    result = data[min_index] * data[max_index]
    return result

import unittest

class TestMaxMinMultiplication(unittest.TestCase):

    def test1(self):
        self.assertEqual(maxMinMultiplication([]), -1)

    def test2(self):
        self.assertEqual(maxMinMultiplication([1]), -1)

    def test3(self):
        self.assertEqual(maxMinMultiplication([2,1]), -1)

    def test4(self):
        self.assertEqual(maxMinMultiplication([10, 5, 15, 2, 7, 12, 18, 1, 3, 6, 8, 11, 13, 17, 19]), 19)

    def test5(self):
        self.assertEqual(maxMinMultiplication([1, 2, 3, None, 5]), -1)  # Важный тест для None
    
    def test6(self):
        self.assertEqual(maxMinMultiplication([7, 5, 8, 3, 6]), 24)
        

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
