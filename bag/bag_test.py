import unittest
from bag import Bag

class TestDynamicArray(unittest.TestCase):
    def test_remove(self):
        test_bag = Bag(initial_capacity=4)
        test_bag.add(3)
        test_bag.add(1)
        test_bag.add(2)
        test_bag.remove(1)
        expected = [3, 2, 0, 0]
        actual = test_bag.get_bag()
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()