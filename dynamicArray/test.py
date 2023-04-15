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

    def test_get_index(self):
        """
        Test the get function
        """
        test_da = DynamicArray(initial_capacity=4)
        test_da.set(1, 1)
        expected = 1
        actual = test_da.get_index(1)
        self.assertEqual(expected, actual)

    def test_append_no_resize(self):
        test_da = DynamicArray(initial_capacity=4)
        test_da.append(1)
        test_da.append(2)
        test_da.append(3)
        expected = 3
        actual = test_da.get_index(2)
        self.assertEqual(expected, actual)

    def test_append_with_resize(self):
        test_da = DynamicArray(initial_capacity=2)
        test_da.append(1)
        test_da.append(2)
        test_da.append(3)
        expected = 3
        actual = test_da.get_index(2)
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()