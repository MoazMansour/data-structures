class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def search(self, find_val):
        if self.left or self.right:
            if self.left.value == find_val or self.right.value == find_val:
                return True
            else:
                return self.left.search(find_val) or self.right.search(find_val)
        return False

    def print_node(self):
        value = [self.value]
        if self.left:
            value += self.left.print_node()
        if self.right:
            value += self.right.print_node()
        return value

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        """Return True if the value
        is in the tree, return
        False otherwise."""
        current = self.root
        if current.value == find_val:
            return True
        return current.search(find_val)

    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        current = self.root
        tree = current.print_node()
        tree_string = ""
        for item in tree:
            tree_string += "-"+str(item)
        return tree_string[1:]


    def preorder_search(self, start, find_val):
        """Helper method - use this to create a
        recursive search solution."""
        return False

    def preorder_print(self, start, traversal):
        """Helper method - use this to create a
        recursive print solution."""
        return traversal


# Set up tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

# Test search
# Should be True
print tree.search(4)
# Should be False
print tree.search(6)

# Test print_tree
# Should be 1-2-4-5-3
print tree.print_tree()
