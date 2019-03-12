class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        current = self.root
        notPlaced = True
        while notPlaced:
            if new_val < current.value:
                if not current.left:
                    current.left = Node(new_val)
                    notPlaced = False
                current = current.left
            else:
                if not current.right:
                    current.right = Node(new_val)
                    notPlaced = False
                current = current.right

    def search(self, find_val):
        current = self.root
        if current.value == find_val:
            return True
        notFound = True
        while notFound:
            if find_val < current.value:
                if not current.left:
                    return False
                    notFound = False
                current = current.left
            elif find_val > current.value:
                if not current.right:
                    return False
                    notFound = False
                current = current.right
            else:
                return True
                notFound = False

# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print tree.search(4)
# Should be False
print tree.search(6)
