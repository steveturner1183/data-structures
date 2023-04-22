import unittest
from binary_search_tree import BST


class TestQue(unittest.TestCase):
    def test_add_1(self):
        tree = BST()
        tree.add(10)
        tree.add(15)
        tree.add(5)
        tree.add(15)
        tree.add(15)
        tree.add(5)
        expected = [10, 5, 5, 15, 15, 15]
        actual = tree.pre_order_traversal()
        self.assertEqual(expected, actual)

    def test_add_2(self):
        expected = [10, -1, 5, -1, 10]
        tree = BST()
        tree.add(10)
        tree.add(10)
        tree.add(-1)
        tree.add(5)
        tree.add(-1)
        actual = tree.pre_order_traversal()
        self.assertEqual(expected, actual)

    def test_contains_1(self):
        tree = BST([10, 15, 5])
        self.assertTrue(tree.contains(15))

    def test_contains_2(self):
        tree = BST([10, 15, 5])
        self.assertFalse(tree.contains(-10))

    def test_contains_3(self):
        tree = BST([10, 15, 5])
        self.assertTrue(tree.contains(15))

    def test_get_first_1(self):
        tree = BST([10, 15, 5])
        expected = 10
        actual = tree.get_first()
        self.assertEqual(expected, actual)

    def test_get_first_2(self):
        tree = BST()
        actual = tree.get_first()
        self.assertIsNone(actual)

    def test_remove_1(self):
        tree = BST([10, 20, 5, 15, 17, 7, 12])
        tree.remove(20)
        expected = [10, 5, 7, 15, 12, 17]
        actual = tree.pre_order_traversal()
        self.assertEqual(expected, actual)

    def test_remove_2(self):

        tree = BST([10, 5, 20, 18, 12, 7, 27, 22, 18, 24, 22, 30])
        tree.remove(20)

        actual = [
            tree.pre_order_traversal()#,
            #tree.in_order_traversal(),
            #tree.post_order_traversal(),
            #tree.by_level_traversal(),
        ]

        expected = [
            [10, 5, 7, 22, 18, 12, 18, 27, 24, 22, 30]#,
            #[5, 7, 10, 12, 18, 18, 22, 22, 24, 27, 30],
            #[7, 5, 12, 18, 18, 22, 24, 30, 27, 22, 10],
            #[10, 5, 22, 7, 18, 27, 12, 18, 24, 30, 22]
        ]

        self.assertEqual(expected, actual)

    def test_remove_3(self):
        tree = BST([10, 20, 5, 15, 17, 7, 12])
        tree.remove(5)
        expected = [10, 7, 20, 15, 12, 17]

        actual = tree.pre_order_traversal()
        self.assertEqual(expected, actual)

    def test_remove_4(self):
        tree = BST([10, 20, 5, 15, 17, 7, 12])
        tree.remove(5)
        tree.remove(7)
        expected = [10, 20, 15, 12, 17]

        actual = tree.pre_order_traversal()
        self.assertEqual(expected, actual)



    def test_remove_first_1(self):
        tree = BST([10, 15, 5])
        tree.remove_first()
        expected = [15, 5]
        actual = tree.pre_order_traversal()
        self.assertEqual(expected, actual)

    def test_remove_first_2(self):
        tree = BST([10, 20, 5, 15, 17, 7])
        tree.remove_first()
        expected = [15, 5, 7, 20, 17]
        actual = tree.pre_order_traversal()
        self.assertEqual(expected, actual)

    def test_remove_first_3(self):
        tree = BST([10, 10, -1, 5, -1])
        tree.remove_first()
        self.assertEqual(tree.pre_order_traversal(), [10, -1, 5, -1])
        tree.remove_first()
        self.assertEqual(tree.pre_order_traversal(), [-1, 5, -1])
        tree.remove_first()
        self.assertEqual(tree.pre_order_traversal(), [5, -1])
        tree.remove_first()
        self.assertEqual(tree.pre_order_traversal(), [-1])
        tree.remove_first()
        self.assertEqual(tree.pre_order_traversal(), [])
        actual = tree.remove_first()
        # All leaves removed
        self.assertFalse(actual)
    
"""
    def test_pre_order_traversal_1(self):
        tree = BST([10, 20, 5, 15, 17, 7, 12])
        expected = [10, 5, 7, 20, 15, 12, 17]
        actual = tree.pre_order_traversal()
        self.assertEqual(expected, actual)

    def test_pre_order_traversal_2(self):
        tree = BST([10, 10, -1, 5, -1])
        expected = [ 10, -1, 5, -1, 10]
        actual = tree.pre_order_traversal()
        self.assertEqual(expected, actual)

    def test_in_order_traversal_1(self):
        tree = BST([10, 20, 5, 15, 17, 7, 12])
        expected = [5, 7, 10, 12, 15, 17, 20]
        actual = tree.in_order_traversal()
        self.assertEqual(expected, actual)

    def test_in_order_traversal_2(self):
        tree = BST([10, 10, -1, 5, -1])
        expected = [-1, -1, 5, 10, 10]
        actual = tree.in_order_traversal()
        self.assertEqual(expected, actual)

    def test_post_order_traversal_1(self):
        tree = BST([10, 20, 5, 15, 17, 7, 12])
        expected = [7, 5, 12, 17, 15, 20, 10]
        actual = tree.post_order_traversal()
        self.assertEqual(expected, actual)

    def test_post_order_traversal_2(self):
        tree = BST([10, 10, -1, 5, -1])
        expected = [-1, 5, -1, 10, 10]
        actual = tree.post_order_traversal()
        self.assertEqual(expected, actual)

    def test_by_level_traversal_1(self):
        tree = BST([10, 20, 5, 15, 17, 7, 12])
        expected = [10, 5, 20, 7, 15, 12, 17]
        actual = tree.by_level_traversal()
        self.assertEqual(expected, actual)

    def test_by_level_traversal_2(self):
        tree = BST([10, 10, -1, 5, -1])
        expected = [10, -1, 10, 5, -1]
        actual = tree.by_level_traversal()
        self.assertEqual(expected, actual)

    def test_size(self):
        pass

    def test_height(self):
        pass

    def test_count_leaves(self):
        pass

    def test_count_unique(self):
        pass

    def test_is_complete(self):
        pass

    def test_is_full(self):
        pass

    def test_is_perfect(self):
        pass

    def comprehensive_test(self):
        tree = BST()

        expected = [
         #  Size Height Leaves Unique Complete   Full   Perfect VALUE
            [0,    -1,     0,      0,    True,    True,   True],  # N/A
            [1,     0,     1,      1,    True,    True,   True],  # 10
            [2,     1,     1,      2,    True,    False,   False],  # 5
            [3,     2,     1,      3,    False,    False,   False],  # 3
            [4,     2,     2,      4,    True,    False,   False],  # 15
            [5,     2,     2,      5,    False,    False,   False],  # 12
            [6,     2,     3,      6,    True,    False,   False],  # 8
            [7,     2,     4,      7,    True,    True,   True],  # 20
            [8,     3,     4,      8,    True,    False,   False],  # 1
            [9,     3,     5,      9,    True,    True,   False],  # 4
            [10,    3,     5,      10,    False,    False,   False],  # 9
            [11,    3,     6,      11,    True,    True,   False],  # 7
        ]

        actual = []
        for value in [10, 5, 3, 15, 12, 8, 20, 1, 4, 9, 7]:
            tree.add(value)
            cur_tree = [
                tree.size(),
                tree.height(),
                tree.count_leaves(),
                tree.count_unique(),
                tree.is_complete(),
                tree.is_full(),
                tree.is_perfect()
            ]
            actual.append(cur_tree)

        self.assertEqual(expected, actual)
        """
