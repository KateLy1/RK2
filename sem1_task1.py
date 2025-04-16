#найти корень числа (ближайшее целое)
def binarySearchSqrt(target):
    if target < 0:
        return None
    l = 0
    r = target
    while l <= r:
        middle = l + (r-l)//2
        if (middle)**2 > target:
            r = middle-1
            continue
        if (middle)**2 < target:
            l = middle+1
            continue
        return middle
    return r

import unittest

class TestBinarySearchSqr(unittest.TestCase):

    def test1(self):
        self.assertEqual(binarySearchSqrt(25), 5)

    def test2(self):
        self.assertEqual(binarySearchSqrt(0), 0)

    def test3(self):
        self.assertIsNone(binarySearchSqrt(-5))

    def test4(self):
        self.assertEqual(binarySearchSqrt(8), 2)
        
    def test5(self):
        self.assertEqual(binarySearchSqrt(15), 3)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
