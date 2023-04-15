import unittest
from linked_list import LinkedList


class TestQue(unittest.TestCase):
    def test_get_and_add_front(self):
        expected = 1
        test_ll = LinkedList()
        test_ll.add_front(1)
        actual = test_ll.get_front()
        self.assertEqual(expected, actual)

    def test_lenth(self):
        pass

    def test_add_back(self):
        pass

    def test_insert_at_index(self, value, index):
        pass

    def test_remove_front(self):
        pass

    def test_remove_back(self):
        pass

    def test_remove_at_index(self, index):
        pass

    def test_get_front(self):
        pass

    def test_get_back(self):
        pass

    def test_remove_value(self, value):
        pass

    def test_count(self, value):
        pass

    def test_slice(self, start, size):
        pass

if __name__ == "__main__":
    unittest.main()
