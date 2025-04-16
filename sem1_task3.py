#В небольшом зоопарке есть некоторое количество животных.
#Каждое животное потребляет какой-то объем еды, выраженный в целочисленном значении. Например, еноту нужна 1-порция еды, зебре 2, пантере 3, льву 4, жирафу 8 и т.д.
#Каждый день, смотритель зоопарка привозит еду такими же порциями. То есть за раз он привозит 8, 3, 9, 1, 7. Порция на 8 может накормить одно животное один раз. То есть такая порция может накормить либо енота, либо льва, либо жирафа, но не может накормить, например зебру и енота. Только кого-то одного.
#Надо написать функцию, которая определит, сколько из переданных животных может накормить заданное количество еды.
#Наивная реализация
def feedAnimals1(animals, food):
    if len(animals) == 0 or len(food) == 0:
        return 0
    count = 0
    feed_an = []
    eaten = []
    i = 0
    while i < (len(food)):
        j = 0
        while j < (len(animals)):
            if food[i] >= animals[j] and i not in eaten and j not in feed_an:
                count += 1
                feed_an.append(j)
                eaten.append(i)
            j += 1
        i += 1
    return count

import unittest

class TestFeedAnimals1(unittest.TestCase):

    def test1(self):
        self.assertEqual(feedAnimals1([], []), 0)

    def test2(self):
        self.assertEqual(feedAnimals1([], 4), 0)

    def test3(self):
        self.assertEqual(feedAnimals1([1], []), 0)

    def test4(self):
        self.assertEqual(feedAnimals1([15], [4]), 0)
        
    def test5(self):
        self.assertEqual(feedAnimals1([4, 2, 7, 1, 23, 4], [1, 5, 2, 1, 21, 6, 7, 4]), 5)
        
    def test6(self):
        self.assertEqual(feedAnimals1([8, 2, 3, 2], [1, 4, 3, 8]), 3)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

#Сортировка

def feedAnimals2(animals, food):
    if len(animals) == 0 or len(food) == 0:
        return 0
    animals.sort()
    food.sort()
    count = 0
    for f in food:
        if f >= animals[count]:
            count += 1
        if count == len(animals):
            break
    return count

import unittest

class TestFeedAnimals2(unittest.TestCase):

    def test1(self):
        self.assertEqual(feedAnimals2([], []), 0)

    def test2(self):
        self.assertEqual(feedAnimals2([], 4), 0)

    def test3(self):
        self.assertEqual(feedAnimals2([1], []), 0)

    def test4(self):
        self.assertEqual(feedAnimals2([15], [4]), 0)
        
    def test5(self):
        self.assertEqual(feedAnimals2([4, 2, 7, 1, 23, 4], [1, 5, 2, 1, 21, 6, 7, 4]), 5)
        
    def test6(self):
        self.assertEqual(feedAnimals2([8, 2, 3, 2], [1, 4, 3, 8]), 3)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
