class Node:
    """
    Node for use in linked list
    """
    def __init__(self, value):
        self.next = None
        self.value = value


class LinkedList:
    """
    Implementation of singly linked list
    """
    def __init__(self):
        self._head = Node(None)
        self._tail = Node(None)
        self._head.next = self._tail

    ###########################################################################
    # Private helper functions                                                #
    ###########################################################################

    def _insert_node(self, front, insert):
        """
        Inserts a Node between two other nodes
        :param front: front node to attach
        :param insert: node to be inserted
        :param back: back node to attach
        :return: None
        """
        temp_next = front.next
        front.next = insert
        insert.next = temp_next
        return

    def _remove_node(self, prev_node, remove_node):
        """
        Removes a Node between two other nodes
        :param prev_node: front node to attach
        :param remove_node: node to be removed
        :return: None
        """
        prev_node.next = remove_node.next
        return

    ###########################################################################
    # Public Linked List functions                                            #
    ###########################################################################

    def length(self, cur_node=None):
        """
        Returns length of linked list
        :return: length of linked list
        """
        if cur_node is None:
            cur_node = self._head.next

        if cur_node == self._tail:
            return 0

        return 1 + self.length(cur_node.next)

    def add_front(self, value):
        """
        Add value to the front of linked list
        :param value: Value to be inserted
        :return: None
        """
        new_node = Node(value)
        self._insert_node(self._head, new_node)
        return

    def remove_front(self):
        """
        Remove value at the front of the linked list
        :return: None
        """
        self._head.next = self._head.next.next

    def get_front(self):
        """
        Return value at the front of the linked list
        :return: Value at front
        """
        return self._head.next.value

    def add_back(self, value, cur_node=None):
        """
        Add value to the back of the linked list
        :param value: Value to be inserted
        :param cur_node: Current node
        :return: None
        """
        if cur_node is None:
            cur_node = self._head

        if cur_node.next == self._tail:
            new_node = Node(value)
            self._insert_node(cur_node, new_node)
            return

        return self.add_back(value, cur_node.next)

    def remove_back(self, prev_node=None, cur_node=None):
        """
        Remove value at the back of the linked list
        :return: None
        """
        if cur_node is None:
            prev_node = self._head
            cur_node = self._head.next

        if cur_node.next == self._tail:
            self._remove_node(prev_node, cur_node)
            return

        return self.remove_back(cur_node, cur_node.next)

    def get_back(self, cur_node=None):
        """
        return value at the back of linked list
        :param cur_node: Current node
        :return: Value at back
        """
        if cur_node is None:
            cur_node = self._head

        if cur_node.next == self._tail:
            return cur_node.value

        return self.get_back(cur_node.next)

    def get_at_index(self, target_index, cur_node=None, cur_index=0):
        """
        Get value at given index
        :param target_index: index to be found
        :param cur_node: current node
        :param cur_index: current index
        :return: Value at given index
        """
        if cur_node is None:
            cur_node = self._head

        if cur_index == target_index:
            return cur_node.value

        return self.get_at_index(target_index, cur_node.next, cur_index + 1)

    def insert_at_index(self, value, target_index, cur_node=None, cur_index=0):
        """
        Insert value at given index
        :param value: Value to be inserted
        :param target_index: Index for insertion
        :param cur_node: current node
        :param cur_index: current index
        :return: None
        """
        if cur_node is None:
            cur_node = self._head

        if cur_index == target_index-1:
            new_node = Node(value)
            self._insert_node(cur_node, new_node)
            return

        return self.insert_at_index(value, target_index, cur_node.next,
                                    cur_index+1)

    def remove_at_index(self, index):
        """
        Remove value at a given index
        :param index: index value is to be removed at
        :return: None
        """
        pass

    def remove_value(self, value):
        """
        Removes given value from the list
        :param value: Value to be removed
        :return: None
        """
        pass

    def count(self, value):
        """
        Returns count of nodes that match given value
        :param value: Value to be counted
        :return: Count of value
        """
        pass

    def slice(self, start, size):
        """
        Returns new linked list with value only from start to size
        :param start: Slice start
        :param size: Amount to slice
        :return: New sliced linked list
        """
        pass