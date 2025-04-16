#Вариант 1 (если у слов одинаковые ASCII не работает)
def ascii_word(word):
    a = 0
    for char in word:
        a += ord(char)
    return a

def anagramm1(data):
    groups = {}
    for i in range(len(data)):
        if ascii_word(data[i]) in groups:
            groups[ascii_word(data[i])].append(data[i])
        else:
            groups[ascii_word(data[i])] = [data[i]]
    return list(groups.values())

import unittest

class TestAnagramm1(unittest.TestCase):

    def test1(self):
        self.assertEqual(anagramm1(["eat","tea","tan","ate","nat","bat"]), [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']])

    def test2(self):
        self.assertEqual(anagramm1(["won","now","aaa","ooo","ooo"]), [["won","now"], ["aaa"],["ooo", "ooo"]])

    def test3(self):
        self.assertEqual(anagramm1([]), [] )

    def test4(self):
        self.assertEqual(anagramm1(['abb', 'aac', 'aca', 'bab']), [['abb', 'bab'], ['acc', 'aca']])
        

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)


  #Вариант 2

def anagramm2(data):
    groups = {}
    for word in data:
        s = ''.join(sorted(word))
        if s in groups:
            groups[s].append(word)
        else:
            groups[s] = [word]
    return list(groups.values())

import unittest

class TestAnagramm2(unittest.TestCase):

    def test1(self):
        self.assertEqual(anagramm2(["eat","tea","tan","ate","nat","bat"]), [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']])

    def test2(self):
        self.assertEqual(anagramm2(["won","now","aaa","ooo","ooo"]), [["won","now"], ["aaa"],["ooo", "ooo"]])

    def test3(self):
        self.assertEqual(anagramm2([]), [] )

    def test4(self):
        self.assertEqual(anagramm2(['abb', 'aac', 'aca', 'bab']), [['abb', 'bab'], ['aac', 'aca']])
        

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
