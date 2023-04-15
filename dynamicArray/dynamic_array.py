class DynamicArray:
    """
    Implementation of dynamic array with add, insert, remove, and delete
    methods
    """
    def __init__(self, initial_capacity):
        self._size = 0
        self._capacity = initial_capacity
        self._data = [0] * initial_capacity

    ###########################################################################
    # Private Helper Functions
    ###########################################################################

    def _copy_contents(self, arr):
        """
        Copies the contents of self._data to a new array
        :param arr: Empty array
        :return: Array with copied contents
        """
        pass

    def _grow_array(self):
        """
        Creates a new array of double the size of capacity, and copies over
        data from self._data array
        :return: None
        """
        pass

    ###########################################################################
    # Public Dynamic Array Functions
    ###########################################################################
    def get_arr(self):
        """
        Retrieve the entire array
        :return: Array object
        """
        return self._data

    def get_index(self, index):
        """
        Retrieve element at given index
        :param index: Index to have element retrieved
        :return: Element at given index
        """
        return self._data[index]

    def set(self, index, value):
        """
        Change value at given index
        :param index: Index to have element changed
        :param value: Value to be set
        :return:
        """
        self._data[index] = value
        return

    def append(self, value):
        """
        Add element to the end of array
        :param value: Value to be appended
        :return: None
        """
        self._data[self._size] = value
        self._size += 1
        return

    def insert(self, index):
        """
        Insert element at a given index. Shift elements after given index
        forward
        :param index:
        :return: None
        """
        pass

    def remove(self):
        """
        Remove element from the end of array
        :return: None
        """
        pass

    def delete(self, index):
        """
        Delete element at given index
        :param index:
        :return: None
        """
        pass