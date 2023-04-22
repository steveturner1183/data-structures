class TreeNode:
    """
    Binary Search Tree Node
    """

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return repr(self.value)


class BST:
    def __init__(self, start_tree=None) -> None:
        self.root = None

        # Populate with existing tree
        if start_tree is not None:
            for value in start_tree:
                self.add(value)

    ##########################################################################
    #  Private helper functions                                              #
    ##########################################################################

    @staticmethod
    def _swap_node(node, parent, new_node=None):
        """
        Helper function to swap one node with another
        :param node: Node to be replaced
        :param parent: Parent of node to be replaced
        :param new_node: New node to replace node with
        :return: None
        """

        # Assign new node to parent
        if node == parent.left:
            parent.left = new_node
        elif node == parent.right:
            parent.right = new_node

        if new_node is None:
            return

        # Assign deleted node's children to new node
        if new_node != node.right and new_node != node.left:
            new_node.left = node.left
            new_node.right = node.right

        return

    @staticmethod
    def _delete_node(node, parent):
        """
        Delete a node between two other nodes, i.e. make child of node
        the new child of the parent
        :param node: Node to be deleted
        :param parent: Parent to take on Nodes child as its own child
        :return:
        """
        # Find successor for node with single child
        if node.left is not None:
            successor = node.left
        elif node.right is not None:
            successor = node.right
        else:
            successor = None

        # Assign new node to parent
        if node == parent.left:
            parent.left = successor
        elif node == parent.right:
            parent.right = successor

        return

    @staticmethod
    def _extract_successor(node):
        """
        Find the in order successor of given node and break connection
        :param node: Node to find in order successor of
        :return: In or successor with existing connections broken
        """
        parent = node
        successor = node.right

        while successor.left is not None:  # search for in order successor
            parent = successor
            successor = successor.left

        if successor == parent.left:  # break successors existing connection
            parent.left = successor.right
        if successor == parent.right:
            parent.right = successor.right

        return successor

    ##########################################################################
    #  Public BST functions                                                  #
    ##########################################################################

    def add(self, value, node=None):
        """
        Adds value to bst
        :param value: Value to be added
        :param node: Current node
        :return: None
        """
        if self.root is None:  # Empty tree, make node the root
            self.root = TreeNode(value)
            return

        if node is None:  # Starting case
            node = self.root

        if value < node.value:  # Traverse left
            if node.left is None:
                node.left = TreeNode(value)
                return
            else:
                return self.add(value, node.left)

        elif value >= node.value:  # Traverse right
            if node.right is None:
                node.right = TreeNode(value)
                return
            else:
                return self.add(value, node.right)

    def contains(self, value, node=None):
        """
        Checks if tree contains node with given value
        :param value: Value to be found
        :param node: Current node
        :return: True if value is in true, false if not found
        """
        if node is None:  # Starting case
            node = self.root

        if node.value == value:
            return True

        if value < node.value:  # Traverse left
            if node.left is None:
                return False
            else:
                return self.contains(value, node.left)

        elif value >= node.value:  # Traverse right
            if node.right is None:
                return False
            else:
                return self.contains(value, node.right)

    def get_first(self):
        """
        Returns the first value in the BST
        :return: First value in tree
        """
        if self.root is not None:
            return self.root.value
        else:
            return self.root

    def remove_first(self):
        """
        Removes the first value in the BST
        :return: None
        """
        if self.root is None:
            return False

        elif self.root.left is None and self.root.right is None:
            self.root = None

        elif self.root.left is not None and self.root.right is None:
            self.root = self.root.left

        elif self.root.left is None and self.root.right is not None:
            self.root = self.root.right

        else:
            successor = self._extract_successor(self.root)
            successor.left = self.root.left
            successor.right = self.root.right
            self.root = successor
        return self.root

    def remove(self, value, parent=None, node=None):
        """
        Removes node by value
        :param value: value to be removed
        :return: None
        """
        if node is None:
            node = self.root

        if node.value == value:  # Node found
            # Case 1 - No child nodes
            if node.left is None and node.right is None:
                self._delete_node(node, parent)

            # Case 2 - Both children
            elif node.left is not None and node.right is not None:
                successor = self._extract_successor(node)
                self._swap_node(node, parent, successor)

            # Case 3 - Single Child
            else:
                self._delete_node(node, parent)

        else:
            if value < node.value:
                self.remove(value, node, node.left)
            else:
                self.remove(value, node, node.right)

    def pre_order_traversal(self, node=None, trav_list=None):
        """
        Returns List containing pre-order traversal
        :param: node: current node
        :param: trav_list: current list of visited nodes
        :return: List with pre-order traversal
        """
        if trav_list is None:
            node = self.root
            trav_list = []

        if node is not None:
            trav_list.append(node.value)
            self.pre_order_traversal(node.left, trav_list)
            self.pre_order_traversal(node.right, trav_list)

        return trav_list

    def in_order_traversal(self, node=None, trav_list=None):
        """
        :param: node: current node
        :param: trav_list: current list of visited nodes
        :return: List with in-order traversal of BST
        """
        if trav_list is None:
            node = self.root
            trav_list = []

        if node is not None:
            self.in_order_traversal(node.left, trav_list)
            trav_list.append(node.value)
            self.in_order_traversal(node.right, trav_list)

        return trav_list

    def post_order_traversal(self, node=None, trav_list=None):
        """
        Returns List containing post-order traversal
        :param: node: current node
        :param: trav_list: current list of visited nodes
        :return: List with post-order traversal
        """
        if trav_list is None:
            node = self.root
            trav_list = []

        if node is not None:
            self.post_order_traversal(node.left, trav_list)
            self.post_order_traversal(node.right, trav_list)
            trav_list.append(node.value)

        return trav_list

    def by_level_traversal(self):
        """
        Returns List containing by-level traversal
        :return: List with by-level traversal
        """
        by_level_list = []
        temp_list = [self.root]

        while len(temp_list) > 0:
            node = temp_list.pop(0)

            if node is not None:
                by_level_list.append(node.value)  # log visit
                temp_list.append(node.left)
                temp_list.append(node.right)

        return by_level_list



    def is_full(self):
        """
        Returns if the tree is full
        :return: True if full, false if not
        """
        pass

    def is_complete(self):
        """
        Returns if the tree is complete
        :return: True if complete, false if not
        """
        pass

    def is_perfect(self):
        """
        Returns if the tree is perfect
        :return: True if perfect, false if not
        """
        pass

    def size(self):
        """
        :return: size of tree
        """
        pass

    def height(self) -> int:
        """
        :return: height of tree
        """
        pass

    def count_leaves(self) -> int:
        """
        :return: leaves in tree
        """
        pass

    def count_unique(self) -> int:
        """
        :return: unique values in tree
        """
        pass
