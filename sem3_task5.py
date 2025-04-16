#На вход функции передается указатель на
#корень бинарного дерева поиска.
#Необходимо для каждого узла проставить
#balance factor
class Node:
    def __init__ (self, data = 0, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right


def calculateHeightsAndBalance(node):
    if node is None:
        return 0
    leftHeight = calculateHeightsAndBalance(node.left)
    rightHeight = calculateHeightsAndBalance(node.right)
    node.balanceFactor = leftHeight - rightHeight
    return 1 + max(leftHeight, rightHeight)

class TestCalculateHeightsAndBalance(unittest.TestCase):

    def test1(self):
        root = None
        calculateHeightsAndBalance(root)
        self.assertEqual(root, None)

    def test2(self):
        root = Node(1)
        calculateHeightsAndBalance(root)
        self.assertEqual(root.balanceFactor, 0)

    def test3(self):
        root = Node(3)
        root.left = Node(2)
        root.left.left = Node(1)
        calculateHeightsAndBalance(root)
        self.assertEqual(root.balanceFactor, 2)
        self.assertEqual(root.left.balanceFactor, 1)
        self.assertEqual(root.left.left.balanceFactor, 0)


    def test4(self):
        root = Node(1)
        root.right = Node(2)
        root.right.right = Node(3)
        calculateHeightsAndBalance(root)
        self.assertEqual(root.balanceFactor, -2)
        self.assertEqual(root.right.balanceFactor, -1)
        self.assertEqual(root.right.right.balanceFactor, 0)


    def test5(self):
        root = Node(2)
        root.left = Node(1)
        root.right = Node(3)
        calculateHeightsAndBalance(root)
        self.assertEqual(root.balanceFactor, 0)
        self.assertEqual(root.left.balanceFactor, 0)
        self.assertEqual(root.right.balanceFactor, 0)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
