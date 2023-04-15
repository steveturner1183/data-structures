import unittest
from que import Que

class TestQue(unittest.TestCase):
    def test_enque(self):
        test_que = Que(initial_capacity=4)
        test_que.enque(1)
        test_que.enque(2)
        expected = [1, 2, 0, 0]
        actual = test_que.get_que()
        self.assertEqual(expected, actual)

    def test_deque(self):
        test_que = Que(initial_capacity=4)
        test_que.enque(1)
        test_que.enque(2)
        expected = 1
        actual = test_que.deque()
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()
