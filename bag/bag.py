from dynamic_array.dynamic_array import DynamicArray

class Bag:
    """
    Bag ADT with add, remove, clear, count, size, display, and equal check
    build off existing dynamic array object
    """
    def __init__(self, initial_capacity):
        self._bag = DynamicArray(initial_capacity=initial_capacity)

    def append(self, value):
        """
        Add item to end of bag
        :return: None
        """
        self._bag.append(value)
