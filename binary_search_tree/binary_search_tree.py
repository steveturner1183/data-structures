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

    def add(self, value, node=None):
        """
        Adds value to bst
        :param value: Value to be added
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
        pass

    def remove(self, value, parent=None, node=None):
        """
        Removes node by value
        :param value: value to be removed
        :return: None
        """
        if node is None:
            node = self.root

        if node.value == value:  # Node found
            if node.left is None and node.right is None:
                self._swap_node(node, parent)
            elif node.left is not None and node.right is None:
                self._swap_node(node, parent, node.left)
            elif node.left is None and node.right is not None:
                self._swap_node(node, parent, node.right)
            elif node.left is not None and node.right is not None:
                successor = self.in_order_successor(node)
                self._swap_node(node, parent, successor)
        else:
            if value < node.value:
                self.remove(value, node, node.left)
            else:
                self.remove(value, node, node.right)

    def _swap_node(self, node, parent, new_node=None):
        if node == parent.left:
            parent.left = new_node
        elif node == parent.right:
            parent.right = new_node
        if new_node is None:
            return
        if new_node != node.right and new_node != node.left:
            new_node.left = node.left
            new_node.right = node.right
        return

    def in_order_successor(self, node):
        parent = node
        node = node.right

        while node.left is not None:
            parent = node
            node = node.left

        if node == parent.left:
            parent.left = node.right
        if node == parent.right:
            parent.right = node.right

        return node

    def pre_order_traversal(self, node=None, trav_list=None):
        """
        Returns List containing pre-order traversal
        :return: List with pre-order traversal
        """
        if trav_list is None:
            node = self.root
            trav_list = []

        if node is None:
            return
        else:
            trav_list.append(node.value)

            self.pre_order_traversal(node.left, trav_list)
            self.pre_order_traversal(node.right, trav_list)

        return trav_list

    def in_order_traversal(self):
        """
        :return: List with in-order traversal of BST
        """
        pass

    def post_order_traversal(self):
        """
        Returns List containing post-order traversal
        :return: List with post-order traversal
        """
        pass

    def by_level_traversal(self):
        """
        Returns List containing by-level traversal
        :return: List with by-level traversal
        """
        pass

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
