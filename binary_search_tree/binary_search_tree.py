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
        :param parent: Parent of node to be removed
        :param node: Node to be removed
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

    def is_full(self, node=None):
        """
        Returns if the tree is full
        :return: True if full, false if not
        """
        if node is None:
            if self.root is None:
                return True
            else:
                return self.is_full(self.root)

        two_children = node.left is not None and node.right is not None
        no_children = node.left is None and node.right is None

        if no_children:
            return True

        if two_children:
            full = self.is_full(node.left)
            if not full:
                return False
            full = self.is_full(node.right)
            if not full:
                return False
            return True

        else:
            return False

    def is_complete(self, first_left=False):
        """
        Returns if the tree is complete. Traverse using by level traversal
        and search for first left only node. Then check that remaining nodes
        ore None
        :return: True if complete, false if not
        """
        if self.root is None:
            return True

        temp_list = [self.root]

        while len(temp_list) > 0:
            node = temp_list.pop(0)

            if first_left is False:
                if node.left is not None and node.right is not None:
                    temp_list.append(node.left)
                    temp_list.append(node.right)
                elif node.left is not None and node.right is None:
                    temp_list.append(node.left)
                    first_left = True
                elif node.left is None and node.right is not None:
                    return False
            else:
                if node.left is not None or node.right is not None:
                    return False

        return True

    def is_perfect(self):
        """
        Returns if the tree is perfect. Perfect tree is a full tree
        where 2^h = number of leaves
        :return: True if perfect, false if not
        """
        # Empty tree
        if self.root is None:
            return True

        # Test if full
        full = self.is_full()
        if not full:
            return False

        # Check leaves on max depth level
        leaves = self.count_leaves()
        height = self.height()

        return 2 ** height == leaves

    def size(self, node=None, tree_size=0):
        """
        :return: size of tree
        """
        if tree_size == 0:
            node = self.root
            if node is None:
                return tree_size

        if node is not None:
            tree_size += 1
            tree_size = self.size(node.left, tree_size)
            tree_size = self.size(node.right, tree_size)

        return tree_size

    def height(self, node=None, tree_height=-1):
        """
        :return: height of tree
        """

        if tree_height == -1:
            node = self.root
            if node is None:
                return tree_height

        if node is not None:
            tree_height += 1
            depth_left = self.height(node.left, tree_height)
            depth_right = self.height(node.right, tree_height)
            max_depth = max(depth_right, depth_left)
            tree_height = max(tree_height, max_depth)

        return tree_height

    def count_leaves(self, node=None, tree_leaves=-1):
        """
        :return: leaves in tree
        """
        if tree_leaves == -1:
            tree_leaves += 1
            node = self.root
            if node is None:
                return tree_leaves

        if node is None:
            return tree_leaves
        elif node.left is None and node.right is None:
            return tree_leaves + 1
        else:
            tree_leaves = self.count_leaves(node.left, tree_leaves)
            tree_leaves = self.count_leaves(node.right, tree_leaves)
            return tree_leaves

    def count_unique(self, node=None, visited=None):
        """
        :return: unique values in tree
        """
        if visited is None:
            node = self.root
            visited = []
            if node is None:
                return 0

        if node is not None:
            if node.value not in visited:
                visited.append(node.value)

            self.count_unique(node.left, visited)
            self.count_unique(node.right, visited)

        return len(visited)
