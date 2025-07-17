class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:

    def insert(self, root, key):
        if not root:
            return Node(key)
        if key < root.value:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        # Left Left Case
        if balance > 1 and key < root.left.value:
            print(f"LL Rotation at node {root.value}")
            return self.rotate_right(root)

        # Right Right Case
        if balance < -1 and key > root.right.value:
            print(f"RR Rotation at node {root.value}")
            return self.rotate_left(root)

        # Left Right Case
        if balance > 1 and key > root.left.value:
            print(f"LR Rotation at node {root.value}")
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)

        # Right Left Case
        if balance < -1 and key < root.right.value:
            print(f"RL Rotation at node {root.value}")
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    def rotate_left(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def rotate_right(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        return x

    def get_height(self, node):
        return node.height if node else 0

    def get_balance(self, node):
        return self.get_height(node.left) - self.get_height(node.right) if node else 0

# ===== Driver Code =====

if __name__ == "__main__":
    avl = AVLTree()
    root = None
    number_of_nodes = int(input())
    node_values = list(map(int, input().split()))
    
    for value in node_values:
        root = avl.insert(root, value)
