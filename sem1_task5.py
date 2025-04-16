#Дан не отсортированный массив целых чисел и некоторое число target. 
#Необходимо написать функцию, которая найдет два таких элемента в массиве, сумма которых будет равна target
#Один элемент можно использовать лишь один раз. В случае если два таких элемента не нашлось, возвращаем пустой массив

def twoSum(data, target):
    cache = {}
    for i in range(len(data)):
        cache[data[i]] = i
    for i in range(len(data)):
        diff = target - data[i]
        if diff in cache and cache[diff] != i:
            return [i, cache[diff]]
    return[]

import unittest

class TestTwoSum(unittest.TestCase):

    def test1(self):
        self.assertEqual(twoSum([], 7), [])

    def test2(self):
        self.assertEqual(twoSum([6, 1, 2, 8, 7], 8), [0, 2])

    def test3(self):
        self.assertEqual(twoSum([5, 3, 9, 10], 20), [] )

    def test4(self):
        self.assertEqual(twoSum([12], 12), [])
        
    def test5(self):
        self.assertEqual(twoSum([-5, -1, 3, 6], 1), [0, 3])
        
    def test6(self):
        self.assertEqual(twoSum([5, 1, 3, 6, 6], 12), [3, 4])
        

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
