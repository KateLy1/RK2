#Как быстро можно сделать N копий документа, используя два ксерокса, каждый копирует со своей скоростью (x и y минут)?

def copyTime(n, x, y):
    if n == 0:
        return 0
    l = 0
    r = (n - 1) * max(x, y)

    while l + 1 < r:
        mid = l + (r-l)//2
        if mid//x + mid//y < n-1:
            l = mid
        else:
            r = mid
    return r + min(x, y)

import unittest

class TestCopyTime(unittest.TestCase):

    def test1(self):
        self.assertEqual(copyTime(1, 2, 5), 2)

    def test2(self):
        self.assertEqual(copyTime(0, 3, 4), 0)

    def test3(self):
        self.assertEqual(copyTime(10, 2, 1), 7)

    def test4(self):
        self.assertEqual(copyTime(10, 1, 2), 7)
        
    def test5(self):
        self.assertEqual(copyTime(5, 2, 2), 6)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
