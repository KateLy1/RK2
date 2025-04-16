#На вход функции подается две строки: a и b. 
#Строка b образована из строки a путем перемешивания и добавления одной буквы. 
#Необходимо вернуть эту букву

#Вариант 1
def extraLetter1(a, b):
    hashMapB = {}
    for i in range(len(b)):
        hashMapB[b[i]] = hashMapB.get(b[i], 0) + 1
    for i in range(len(a)):
        if a[i] in hashMapB:
            hashMapB[a[i]] -= 1
    for letter, count in hashMapB.items():
        if count > 0:
            return letter
    return ""

import unittest

class TestExtraLetter1(unittest.TestCase):

    def test1(self):
        self.assertEqual(extraLetter1('', ''), '')

    def test2(self):
        self.assertEqual(extraLetter1('baba', 'aabbb'), 'b')

    def test3(self):
        self.assertEqual(extraLetter1('ade', 'eda'), '')

    def test4(self):
        self.assertEqual(extraLetter1('uio', 'oeiu'), 'e')
        
    def test5(self):
        self.assertEqual(extraLetter1('fe', 'efo'), 'o')
        

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)


#Вариант 2
#На вход функции подается две строки: a и b. 
#Строка b образована из строки a путем перемешивания и добавления одной буквы. 
#Необходимо вернуть эту букву

def extraLetter2(a, b):
    hashMapA = {}
    for i in range (len(a)):
        hashMapA[a[i]] = hashMapA.get(a[i], 0) + 1
    for i in range (len(b)):
        if b[i] in hashMapA:
            hashMapA[b[i]] -= 1
            if hashMapA[b[i]] == 0:
                del hashMapA[b[i]]
                continue
            continue
        return b[i]
    return ""

import unittest

class TestExtraLetter2(unittest.TestCase):

    def test1(self):
        self.assertEqual(extraLetter2('', ''), '')

    def test2(self):
        self.assertEqual(extraLetter2('baba', 'aabbb'), 'b')

    def test3(self):
        self.assertEqual(extraLetter2('ade', 'eda'), '')

    def test4(self):
        self.assertEqual(extraLetter2('uio', 'oeiu'), 'e')
        
    def test5(self):
        self.assertEqual(extraLetter2('fe', 'efo'), 'o')
        

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
