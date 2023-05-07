import unittest
from avl_tree import AVL


class TestAVL(unittest.TestCase):

    def test_add_1(self):
        test_cases = (
            (1, 2, 3),  # RR
            (3, 2, 1),  # LL
            (1, 3, 2),  # RL
            (3, 1, 2),  # LR
        )
        expected = [2, 1, 3]

        for case in test_cases:
            avl = AVL(case)
            self.assertEqual(expected, avl.pre_order_traversal())

    def test_add_2(self):
        test_cases = [
        [(10, 20, 30, 40, 50), [20, 10, 40, 30, 50]],
        [(30, 20, 10, 5, 1), [20, 5, 1, 10, 30]],
        [(30, 20, 10, 1, 5), [20, 5, 1, 10, 30]],
        [(5, 4, 6, 3, 7, 2, 8), [5, 3, 2, 4, 7, 6, 8]],
        [range(0, 30, 3), [9, 3, 0, 6, 21, 15, 12, 18, 24, 27]],
        [range(0, 31, 3), [9, 3, 0, 6, 21, 15, 12, 18, 27, 24, 30]],
        [range(0, 34, 3), [21, 9, 3, 0, 6, 15, 12, 18, 27, 24, 30, 33]],
        [range(10, -10, -2), [4, -4, -6, -8, 0, -2, 2, 8, 6, 10]],
        [('A', 'B', 'C', 'D', 'E'), ['B', 'A', 'D', 'C', "E"]],
        [(1, 1, 1, 1), [1]]
        ]

        for case in test_cases:
            avl = AVL(case[0])
            expected = case[1]
            actual = avl.pre_order_traversal()
            self.assertEqual(expected, actual)

    """ Only needs run once
    def test_add_3(self):
        import random
        for _ in range(100):
            case = list(set(random.randrange(1, 20000) for _ in range(900)))
            avl = AVL()
            for value in case:
                avl.add(value)
            if not avl.is_valid_avl():
                raise Exception("PROBLEM WITH ADD OPERATION")
    """

    def test_remove_1(self):
        test_cases = (
            ((1, 2, 3), 1, [2, 3]),  # no AVL rotation
            ((1, 2, 3), 2, [3, 1]),  # no AVL rotation
            ((1, 2, 3), 3, [2, 1]),  # no AVL rotation
            ((50, 40, 60, 30, 70, 20, 80, 45), 0, [50, 30, 20, 40, 45, 70, 60, 80]),
            ((50, 40, 60, 30, 70, 20, 80, 45), 45, [50, 30, 20, 40, 70, 60, 80]),  # no AVL rotation
            ((50, 40, 60, 30, 70, 20, 80, 45), 40, [50, 30, 20, 45, 70, 60, 80]),  # no AVL rotation
            ((50, 40, 60, 30, 70, 20, 80, 45), 30, [50, 40, 20, 45, 70, 60, 80]),  # no AVL rotation
        )
        for tree, del_value, expected in test_cases:
            avl = AVL(tree)
            avl.remove(del_value)
            self.assertEqual(expected, avl.pre_order_traversal())
            if not avl.is_valid_avl():
                raise Exception("PROBLEM WITH REMOVE OPERATION")

    def test_remove_2(self):
        test_cases = (
            ((50, 40, 60, 30, 70, 20, 80, 45), 20, [50, 40, 30, 45, 70, 60, 80]),  # RR
            ((50, 40, 60, 30, 70, 20, 80, 15), 40, [50, 20, 15, 30, 70, 60, 80]),  # LL
            ((50, 40, 60, 30, 70, 20, 80, 35), 20, [50, 35, 30, 40, 70, 60, 80]),  # RL
            ((50, 40, 60, 30, 70, 20, 80, 25), 40, [50, 25, 20, 30, 70, 60, 80]),  # LR
        )
        for tree, del_value, expected in test_cases:
            avl = AVL(tree)
            avl.remove(del_value)
            self.assertEqual(expected, avl.pre_order_traversal())
            if not avl.is_valid_avl():
                raise Exception("PROBLEM WITH REMOVE OPERATION")

    def test_remove_3(self):
        expected = [
            [5, -3, -7, -5, 1, -1, 3, 9, 7, 13, 11, 15],
            [5, -3, -5, 1, -1, 3, 9, 7, 13, 11, 15],
            [5, 1, -3, -1, 3, 9, 7, 13, 11, 15],
            [5, 1, -1, 3, 9, 7, 13, 11, 15],
            [5, 1, 3, 9, 7, 13, 11, 15],
            [9, 5, 3, 7, 13, 11, 15],
            [9, 5, 7, 13, 11, 15],
            [9, 7, 13, 11, 15],
            [13, 9, 11, 15],
            [13, 11, 15],
            [13, 15],
            [15],
            []
        ]

        case = range(-9, 16, 2)
        avl = AVL(case)
        i = 0
        for del_value in case:
            avl.remove(del_value)
            self.assertEqual(expected[i], avl.pre_order_traversal())
            i += 1
            if not avl.is_valid_avl():
                raise Exception("PROBLEM WITH REMOVE OPERATION")

    def test_remove_4(self):
        expected = [
            [24, 9, 3, 0, 6, 15, 12, 18, 30, 27, 33],
            [27, 9, 3, 0, 6, 15, 12, 18, 30, 33],
            [9, 3, 0, 6, 30, 15, 12, 18, 33],
            [12, 3, 0, 6, 30, 15, 18, 33],
            [15, 3, 0, 6, 30, 18, 33],
            [18, 3, 0, 6, 30, 33],
            [30, 3, 0, 6, 33],
            [3, 0, 33, 6],
            [6, 0, 33],
            [33, 0]
        ]

        case = range(0, 34, 3)
        avl = AVL(case)
        for _ in case[:-2]:
            avl.remove(avl.root.value)
            if not avl.is_valid_avl():
                raise Exception("PROBLEM WITH REMOVE OPERATION")
