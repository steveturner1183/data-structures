import unittest
from dynamic_array import DynamicArray

class TestDynamicArray(unittest.TestCase):
    def test_set(self):
        test_da = DynamicArray(initial_capacity=4)
        test_da.set(1, 1)
        expected = [0, 1, 0, 0]
        actual = test_da.get_arr()
        self.assertEqual(expected, actual)

    def test_get_index(self):
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

    def test_insert(self):
        test_da = DynamicArray(initial_capacity=4)
        test_da.append(1)
        test_da.append(2)
        test_da.append(4)
        expected = [1, 2, 3, 4]
        test_da.insert(3, 2)
        actual = test_da.get_arr()
        self.assertEqual(expected, actual)

    def test_remove(self):
        test_da = DynamicArray(initial_capacity=4)
        test_da.append(1)
        test_da.append(2)
        test_da.append(3)
        expected = [1, 2, 0, 0]
        test_da.remove()
        actual = test_da.get_arr()
        self.assertEqual(expected, actual)

    def test_delete(self):
        test_da = DynamicArray(initial_capacity=4)
        test_da.append(1)
        test_da.append(2)
        test_da.append(3)
        expected = [1, 3, 0, 0]
        test_da.delete(1)
        actual = test_da.get_arr()
        self.assertEqual(expected, actual)

    def test_slice(self):
        test_da = DynamicArray(initial_capacity=4)
        test_da.append(1)
        test_da.append(2)
        test_da.append(3)
        expected = [3, 0]
        actual = test_da.slice(2, 3)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()