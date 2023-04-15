import unittest
from dynamic_array import DynamicArray

class TestDynamicArray(unittest.TestCase):
    def test_set(self):
        """
        Tests the set function
        """
        test_da = DynamicArray(initial_capacity=4)
        test_da.set(1, 1)
        expected = [0, 1, 0, 0]
        actual = test_da.get_arr()
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()