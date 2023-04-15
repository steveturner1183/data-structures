from dynamic_array.dynamic_array import DynamicArray

class Que:
    """
    Implementation of que using existing dynamic array
    """
    def __init__(self, initial_capacity):
        self._que = DynamicArray(initial_capacity=initial_capacity)

    def enque(self, value):
        """
        Adds value to the back of the que
        :param value: Value to be added
        :return: None
        """
        pass

    def deque(self):
        """
        Removes item from the start of que and returns
        :return: item at the start of the que
        """
        pass