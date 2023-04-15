import unittest
from stack import Stack

class TestQue(unittest.TestCase):
    def test_pop(self):
        test_stack = Stack(initial_capacity=4)
        test_stack.push(1)
        test_stack.push(2)
        test_stack.push(3)
        expected = 2
        test_stack.pop()
        actual = test_stack.pop()
        self.assertEqual(expected, actual)

    def test_push(self):
        test_stack = Stack(initial_capacity=4)
        test_stack.push(1)
        test_stack.push(2)
        test_stack.push(3)
        expected = 3
        actual = test_stack.pop()
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()
