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

    def _copy_contents(self):
        """
        Copies the contents of self._data to a new array
        :return: Array with copied contents
        """
        temp_array = [0] * self._capacity * 2
        for index in range(0, self._size):
            temp_array[index] = self._data[index]
        return temp_array

    def _grow_array(self):
        """
        Creates a new array of double the size of capacity, and copies over
        data from self._data array
        :return: None
        """
        self._data = self._copy_contents()
        self._capacity *= 2

    def _check_capacity(self):
        """
        Checks capacity, and grows array if needed
        :return: None
        """
        if self._size == self._capacity:
            self._grow_array()

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
        self._check_capacity()
        self._data[self._size] = value
        self._size += 1
        return

    def insert(self, value, index):
        """
        Insert element at a given index. Shift elements after given index
        forward
        :param value: Value to be inserted
        :param index: Index valued to be inserted at
        :return: None
        """
        self._check_capacity()

        # Shift elements
        for i in range(self._size, index, -1):
            self._data[i] = self._data[i-1]

        self._data[index] = value
        self._size += 1
        return

    def remove(self):
        """
        Remove element from the end of array
        :return: None
        """
        self._data[self._size-1] = 0
        self._size -= 1
        return

    def delete(self, index):
        """
        Delete element at given index
        :param index:
        :return: None
        """
        # Shift elements
        for i in range(index, self._size):
            self._data[i] = self._data[i+1]

        self._data[self._size] = 0
        self._size -= 1
        return