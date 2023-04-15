from dynamic_array.dynamic_array import DynamicArray


class Stack:
    def __init__(self, initial_capacity):
        self._stack = DynamicArray(initial_capacity=initial_capacity)

    def pop(self):
        """
        Remove and return item from the top of the stack
        :return: Item at the top of the stack
        """
        pop_index = self._stack.get_size()-1

        # Store item to return
        value = self._stack.get_index(pop_index)

        # Remove last item
        self._stack.remove()

        return value

    def push(self, value):
        """
        Add item to the top of the stack
        :return: None
        """
        self._stack.append(value)
