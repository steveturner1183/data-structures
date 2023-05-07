class Stack:
    """
    Class implementing STACK ADT.
    Supported methods are: push, pop, top, is_empty
    DO NOT CHANGE THIS CLASS IN ANY WAY
    YOU ARE ALLOWED TO CREATE AND USE OBJECTS OF THIS CLASS IN YOUR SOLUTION
    """
    def __init__(self):
        """ Initialize empty stack based on Python list """
        self._data = []

    def push(self, value: object) -> None:
        """ Add new element on top of the stack """
        self._data.append(value)

    def pop(self):
        """ Remove element from top of the stack and return its value """
        return self._data.pop()

    def top(self):
        """ Return value of top element without removing from stack """
        return self._data[-1]

    def is_empty(self):
        """ Return True if the stack is empty, return False otherwise """
        return len(self._data) == 0

    def __str__(self):
        """ Return content of the stack as a string (for use with print) """
        data_str = [str(i) for i in self._data]
        return "STACK: { " + ", ".join(data_str) + " }"


class TreeNode:
    """
    AVL Tree Node class
    """
    def __init__(self, value):
        """
        Initialize a new AVL node
        """
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.height = 0

    def __str__(self):
        return 'AVL Node: {}'.format(self.value)

from binary_search_tree import BST


class AVL(BST):
    def __init__(self, start_tree=None):
        super().__init__(start_tree=start_tree)
        self.root = None

        # populate AVL with initial values (if provided)
        if start_tree is not None:
            for value in start_tree:
                self.add(value)

    def is_valid_avl(self) -> bool:
        """
        Perform pre-order traversal of the tree. Return False if there
        are any problems with attributes of any of the nodes in the tree.
        """
        s = Stack()

        s.push(self.root)
        while not s.is_empty():
            node = s.pop()
            if node:
                # check for correct height (relative to children)
                l = node.left.height if node.left else -1
                r = node.right.height if node.right else -1
                if node.height != 1 + max(l, r):
                    return False

                if node.parent:
                    # parent and child pointers are in sync
                    if node.value < node.parent.value:
                        check_node = node.parent.left
                    else:
                        check_node = node.parent.right
                    if check_node != node:
                        return False
                else:
                    # NULL parent is only allowed on the root of the tree
                    if node != self.root:
                        return False
                s.push(node.right)
                s.push(node.left)
        return True

    # -----------------------------------------------------------------------
    @staticmethod
    def balance_factor(node):
        """
        :param node: node to find balance factor of
        :returns: balance factor of given node
        """
        # Find balance of current node
        if node.left is None and node.right is not None:
            node_balance = 1
        elif node.right is None and node.left is not None:
            node_balance = -1
        else:
            node_balance = 0

        # Find balance of children
        child_left = 0 if node.left is None else node.left.height
        child_right = 0 if node.right is None else node.right.height
        child_balance = child_right - child_left

        return node_balance + child_balance

    @staticmethod
    def update_height(node):
        """
        Updates the height of a given node
        """
        # Find potential heights based on left and right children
        height_left = 0 if node.left is None else node.left.height + 1
        height_right = 0 if node.right is None else node.right.height + 1

        node.height = max(height_left, height_right)

    def rotate_left(self, node):
        """
        Rotates the given subtree left in AVL Tree
        :return: New root of subtree
        """
        child = node.right

        node.right = child.left
        if child.left is not None:
            child.left.parent = node

        child.left = node
        node.parent = child

        self.update_height(node)
        self.update_height(child)

        return child

    def rotate_right(self, old_root):
        """
        Rotates the sub tree right
        """
        new_root = old_root.left

        old_root.left = new_root.right
        if new_root.right is not None:
            new_root.right.parent = old_root

        new_root.right = old_root
        old_root.parent = new_root

        self.update_height(old_root)
        self.update_height(new_root)

        return new_root

    def rebalance(self, node):
        """
        Rebalances around given node
        """
        if self.balance_factor(node) < -1:  # imbalance left

            if self.balance_factor(node.left) > 0:  # rotate left for double rotation
                node.left = self.rotate_left(node.left)
                node.left.parent = node.parent

            node_parent = node.parent
            new_root = self.rotate_right(node)  # rotate right
            new_root.parent = node_parent

            # attach node to new sub tree root
            if node == self.root:
                self.root = new_root

            elif node == node_parent.left:
                node_parent.left = new_root
            else:
                node_parent.right = new_root

        elif self.balance_factor(node) > 1:  # imbalance right

            if self.balance_factor(node.right) < 0:  # rotate right for double rotation
                node.right = self.rotate_right(node.right)
                node.right.parent = node.parent

            node_parent = node.parent
            new_root = self.rotate_left(node)  # rotate
            new_root.parent = node_parent

            # attach node to new sub tree root
            if node == self.root:
                self.root = new_root

            elif node == node_parent.left:
                node_parent.left = new_root
            else:
                node_parent.right = new_root

        else:
            self.update_height(node)

    def attach_node(self, node, parent):
        if node.value < parent.value:  # Add to left
            parent.left = node
        else:  # Add to right
            parent.right = node

        node.parent = parent

        return

    def update_subtree_heights(self, subroot):
        node = subroot

        while node.parent is not None:  # update subtree heights
            node.parent.height += 1
            node = node.parent

        return

    def insert_node(self, value):
        """
        inserts a new node to the tree, maintaining BST property
        """
        parent = None
        node = self.root
        new_node = TreeNode(value)

        if self.root is None:  # Empty tree
            self.root = new_node
            return

        while node is not None:  # Search for location to place node
            if value == node.value:  # Invalid - value already in tree
                return None

            parent = node
            # Traverse left or right based on value
            node = node.left if value < node.value else node.right

        self.attach_node(new_node, parent)  # insert new node

        height_node = new_node

        while height_node.parent is not None:  # update subtree heights
            height_node.parent.height += 1
            height_node = height_node.parent

        return new_node

    def remove_first(self):
        """
        Removes the first value at the root node
        """

        node = self.root

        if node.left is None and node.right is None:
            self.root = None
            return node

        elif node.left is not None and node.right is None:
            self.root.left.parent = None
            self.root = self.root.left
            return self.root

        elif node.left is None and node.right is not None:
            self.root.parent = None
            self.root = self.root.right
            return self.root

        elif node.left is not None and node.right is not None:
            # find in order successor
            successor = self.extract_successor(node, node.right)
            successor_parent = successor.parent

            self.root = successor
            successor.parent = None

            self.update_subtree_heights(successor_parent)

            # Balance begins at lowest level affected
            if successor_parent != node:  # Balance at successors parent
                return successor_parent
            else:  # parent is old head, balance at new head
                return successor

    def dettach_node(self, node, child, parent):
        if parent.left == node:
            parent.left = child
        else:
            parent.right = child

        if child is not None:
            child.parent = parent
        self.update_subtree_heights(parent)

    def find_node(self, value):
        # Set initial values
        node = self.root
        parent = None

        while node.value != value:
            parent = node
            # Traverse left or right based on value
            node = node.left if value < node.value else node.right

            if node is None:
                return False  # value is not found

        return node

    def remove_node(self, value):
        """
        Removes first instance of the value in Binary tree. Returns true if node is removed, false if not
        """
        # Remove root if value matches
        if self.root.value == value:
            return self.remove_first()

        # Search for node to be extracted
        node = self.find_node(value)
        if node is False:  # node not found
            return False

        balance_start = node.parent
        parent = node.parent

        # Node has no children and can just be removed
        if node.left is None and node.right is None:
            replacement = None

        # Node only has one child
        elif node.left is not None and node.right is None:  # left child
            replacement = node.left
        elif node.left is None and node.right is not None:  # right child
            replacement = node.right

        # Node has two children
        else:
            replacement = self.extract_successor(node, node.right)

        # Remove node, fill with replacement node
        self.dettach_node(node, replacement, parent)

        if node == self.root:
            replacement.parent = None
            self.root = replacement

        return balance_start

    def extract_successor(self, node, successor):
        # Find in order Successor
        while successor.left is not None:
            successor = successor.left

        # swap node and successor
        successor.left = node.left
        successor.left.parent = successor

        # Move successors right child if successor is a leftmost node
        if successor.parent != node:
            successor.parent.left = successor.right
            if successor.right is not None:
                successor.right.parent = successor.parent

            successor.right = node.right
            successor.right.parent = successor

        return successor

    def add(self, value, cur_node=None):
        """
        Adds a new node to AVL tree
        """
        # insert new node
        node = self.insert_node(value)

        if node is None:  # duplicate value found
            return

        parent = node.parent

        # rebalance tree
        while parent is not None:
            self.rebalance(parent)
            parent = parent.parent

    def remove(self, value, parent=None, node=None):
        """
        Removes a node from the tree maintaining AVL property
        """
        node_parent = self.remove_node(value)

        if node_parent is False:
            return False

        while node_parent is not None:
            self.rebalance(node_parent)
            node_parent = node_parent.parent

        return True
