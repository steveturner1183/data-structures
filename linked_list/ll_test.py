import unittest
from linked_list import LinkedList


class TestQue(unittest.TestCase):
    def test_get_and_add_front(self):
        expected = 1
        test_ll = LinkedList()
        test_ll.add_front(1)
        actual = test_ll.get_front()
        self.assertEqual(expected, actual)

    def test_length(self):
        expected = 3
        test_ll = LinkedList()
        test_ll.add_front(1)
        test_ll.add_front(1)
        test_ll.add_front(1)
        actual = test_ll.length()
        self.assertEqual(expected, actual)

    def test_add_and_get_back(self):
        expected = 2
        test_ll = LinkedList()
        test_ll.add_front(1)
        test_ll.add_back(2)
        actual = test_ll.get_back()
        self.assertEqual(expected, actual)

    def test_insert_at_index(self):
        pass

    def test_remove_front(self):
        pass

    def test_remove_back(self):
        pass

    def test_remove_at_index(self):
        pass

    def test_get_front(self):
        pass

    def test_get_back(self):
        pass

    def test_remove_value(self):
        pass

    def test_count(self):
        pass

    def test_slice(self):
        pass

if __name__ == "__main__":
    unittest.main()
