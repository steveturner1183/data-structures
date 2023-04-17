class TreeNode:
    """
    Binary Search Tree Node
    """

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self, start_tree=None) -> None:
        self.root = None

        # Populate with existing tree
        if start_tree is not None:
            for value in start_tree:
                self.add(value)

    def add(self, value):
        """
        Adds value to bst
        :param value: Value to be added
        :return: None
        """
        pass

    def contains(self, value):
        """
        Checks if tree contains node with given value
        :param value: Value to be found
        :return: True if value is in true, false if not found
        """
        pass

    def get_first(self):
        """
        Returns the first value in the BST
        :return: First value in tree
        """
        pass

    def remove_first(self):
        """
        Removes the first value in the BST
        :return: None
        """
        pass

    def remove(self, value):
        """
        Removes node by value
        :param value: value to be removed
        :return: None
        """
        pass

    def pre_order_traversal(self):
        """
        Returns List containing pre-order traversal
        :return: List with pre-order traversal
        """
        pass

    def in_order_traversal(self):
        """
        Returns List containing in-order traversal
        :return: List with in-order traversal
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
