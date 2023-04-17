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

    def _remove_node(self, prev_node):
        """
        Removes a Node between two other nodes
        :param prev_node: Node before node to be removed
        :return: None
        """
        prev_node.next = prev_node.next.next
        return

    def _find_node_by_index(self, target_index, cur_node=None, cur_index=1):
        """
        Find node at given index
        :param target_index: index to be found
        :param cur_node: current node
        :param cur_index: current index
        :return: Node at given index
        """
        if cur_node is None:
            cur_node = self._head.next

            if cur_node == self._tail:
                raise Exception("Empty List")

        if cur_index == target_index:
            return cur_node

        return self._find_node_by_index(target_index, cur_node.next,
                                        cur_index + 1)

    def _find_last_node(self, cur_node=None):
        """
        Find last node before tail
        :param cur_node: Current node
        :return: Last node before tail
        """
        if cur_node is None:
            cur_node = self._head

        if cur_node.next == self._tail:
            return cur_node

        return self._find_last_node(cur_node.next)

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

    def add_back(self, value):
        """
        Add value to the back of the linked list
        :param value: Value to be inserted
        :param cur_node: Current node
        :return: None
        """
        new_node = Node(value)
        last_node = self._find_last_node()

        self._insert_node(last_node, new_node)

        return

    def remove_back(self, prev_node=None, cur_node=None):
        """
        Remove value at the back of the linked list
        :return: None
        """
        if cur_node is None:
            prev_node = self._head
            cur_node = self._head.next

        if cur_node.next == self._tail:
            self._remove_node(prev_node)
            return

        return self.remove_back(cur_node, cur_node.next)

    def get_back(self):
        """
        return value at the back of linked list
        :param cur_node: Current node
        :return: Value at back
        """
        return self._find_last_node().value

    def get_at_index(self, target_index):
        """
        Get value at given index
        :param target_index: index to be found (1, 2..)
        :param cur_node: current node
        :param cur_index: current index
        :return: Value at given index
        """
        target_node = self._find_node_by_index(target_index)

        return target_node.value

    def insert_at_index(self, value, target_index):
        """
        Insert value at given index
        :param value: Value to be inserted
        :param target_index: Index for insertion (1, 2..)
        :param cur_node: current node
        :param cur_index: current index
        :return: None
        """
        new_node = Node(value)

        # Find node before index to be inserted
        prev_node = self._find_node_by_index(target_index-1)

        self._insert_node(prev_node, new_node)

    def remove_at_index(self, target_index):
        """
        Remove value at a given index
        :param target_index: index value is to be removed at
        :return: None
        """
        prev_node = self._find_node_by_index(target_index-1)
        self._remove_node(prev_node)
        return

    def remove_value(self, value, prev_node=None, cur_node=None):
        """
        Removes first occurance of given value from the list
        :param value: Value to be removed
        :param prev_node: previous node
        :param cur_node: current node
        :return: None
        """
        if cur_node is None:
            prev_node = self._head
            cur_node = self._head.next

        if cur_node.value == value:
            self._remove_node(prev_node)
            return

        return self.remove_value(cur_node, cur_node.next)

    def count(self, value, cur_node=None, count=0):
        """
        Returns count of nodes that match given value
        :param value: Value to be counted
        :param cur_node: current node
        :param count: current count of matched values
        :return: Count of value
        """
        if cur_node is None:
            cur_node = self._head.next

        if cur_node == self._tail:
            return count

        if cur_node.value == value:
            return self.count(value, cur_node.next, count + 1)
        else:
            return self.count(value, cur_node.next, count)
