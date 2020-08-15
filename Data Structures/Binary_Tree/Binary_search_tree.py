class Tree_Node():
    def __init__(self, key = 0):
        self.data = key
        self.left = None
        self.right = None


class Binary_Search_Tree():
    def __init__(self, root):
        root_node = Tree_Node(root)
        self.root = root_node

    def insert(self, key):
        assert type(key) is int, "key is an integer"
        self.root = self.insert_node(self.root, key)
        
    def insert_node(self, node, key):
        if node == None:
            key_node = Tree_Node(key)
            node = key_node
        else:
            if node.data <= key:
                node.left = self.insert_node(node.left, key)
            else:
                node.right = self.insert_node(node.right, key)
        return node



    def height(self):
        # height(node) = max(height(node.left), height(node.right)) + 1
        return self.height_calc(self.root)  

    def height_calc(self, node):
        if node == None:
            return 0
        elif node.left == None and node.right == None:
            return 1
        else:
            return max(self.height_calc(node.left), self.height_calc(node.right)) + 1

    def print_2d(self):

    def print_2d_(self, root, space):
        assert 


