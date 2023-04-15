from dynamic_array.dynamic_array import DynamicArray

class Bag:
    """
    Bag ADT with add, remove, clear, count, size, display, and equal check
    build off existing dynamic array object
    """
    def __init__(self, initial_capacity):
        self._bag = DynamicArray(initial_capacity=initial_capacity)

    ###########################################################################
    # Private Helper Functions                                                #
    ###########################################################################
    def find_index(self, value):
        """
        Searches bag for value at given index. Returns false if value not
        found
        :param value: Required value
        :return: Index of given value
        """
        search_arr = self._bag.get_arr()
        search_end = self._bag.get_size()

        # Search for value
        for i in range(0, search_end+1):
            if search_arr[i] == value:
                return i

        # Value not found
        return False

    ###########################################################################
    # Public Bag Functions                                                    #
    ###########################################################################

    def get_bag(self):
        """
        Show contents of bag
        :return: Bag array
        """
        return self._bag.get_arr()

    def add(self, value):
        """
        Add item to end of bag
        :return: None
        """
        self._bag.append(value)

    def remove(self, value):
        """
        Removes value from bag
        :param value:
        :return: None
        """
        search_index = self.find_index(value)
        if search_index is not False:
            self._bag.delete(search_index)
        else:
            raise Exception("Value not in bag")