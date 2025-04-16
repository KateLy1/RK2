#Вариант 1
#Нужно реализовать алгоритм,
#который перевернет бинарное
#дерево "вверх ногами", т.е.
#поменяет местами левые и правые
#поддеревья каждого узла.
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

def tree_to_list(root):
    if root is None:
        return []
    queue = [root]
    result = []
    while queue:
        node = queue.pop(0)
        if node is not None:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    return result


def mirrorTree(node):
    if (node == None):
        return None
    node.left, node.right = node.right, node.left
    mirrorTree(node.left)
    mirrorTree(node.right)
    return node

class TestMirrorTree(unittest.TestCase):

    def test1(self):
        self.assertIsNone(mirrorTree(None))

    def test2(self):
        root = TreeNode(1)
        mirrored_root = mirrorTree(root)
        self.assertEqual(mirrored_root.val, 1)
        self.assertIsNone(mirrored_root.left)
        self.assertIsNone(mirrored_root.right)

    def test3(self):
        root = TreeNode(1, TreeNode(2), TreeNode(3))
        mirrored_root = mirrorTree(root)
        self.assertEqual(mirrored_root.val, 1)
        self.assertEqual(mirrored_root.left.val, 3)
        self.assertEqual(mirrored_root.right.val, 2)

    def test4(self):
        arr = [1, 2, 3, 4, 5, 6, 7]
        root = buildTree(arr, 0)
        mirrored_root = mirrorTree(root)
        self.assertEqual(tree_to_list(mirrored_root), [1, 3, 2, 7, 6, 5, 4])


    def test5(self):
        root = TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(5))
        mirrored_root = mirrorTree(root)
        expected_arr = [1, 5, 2, None, None, 3, None]
        expected_root = buildTree(expected_arr, 0)
        self.assertEqual(tree_to_list(mirrored_root), tree_to_list(expected_root))


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)


#Вариант2
def mirrorTreeIterative(node):
    if (node == None):
        return None
    queue = [node]
    while (len(queue) > 0):
        current = queue.pop()
        temp = current.left
        current.left = current.right
        current.right = temp
        if (current.left):
            queue.append(current.left)
        if (current.right):
            queue.append(current.right)
    return node


class TestMirrorTreeIterative(unittest.TestCase):

    def test1(self):
        self.assertIsNone(mirrorTreeIterative(None))

    def test2(self):
        root = TreeNode(1)
        mirrored_root = mirrorTreeIterative(root)
        self.assertEqual(mirrored_root.val, 1)
        self.assertIsNone(mirrored_root.left)
        self.assertIsNone(mirrored_root.right)

    def test3(self):
        root = TreeNode(1, TreeNode(2), TreeNode(3))
        mirrored_root = mirrorTreeIterative(root)
        self.assertEqual(mirrored_root.val, 1)
        self.assertEqual(mirrored_root.left.val, 3)
        self.assertEqual(mirrored_root.right.val, 2)

    def test4(self):
        arr = [1, 2, 3, 4, 5, 6, 7]
        root = buildTree(arr, 0)
        mirrored_root = mirrorTreeIterative(root)
        self.assertEqual(tree_to_list(mirrored_root), [1, 3, 2, 7, 6, 5, 4])


    def test5(self):
        root = TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(5))
        mirrored_root = mirrorTree(root)
        expected_arr = [1, 5, 2, None, None, 3, None]
        expected_root = buildTree(expected_arr, 0)
        self.assertEqual(tree_to_list(mirrored_root), tree_to_list(expected_root))


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
